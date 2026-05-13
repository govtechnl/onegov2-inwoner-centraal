"""Layer 4: simulated correspondence stream per organisation.

Drives off `reference/brieven-catalogus.yaml`. For every deceased person we
roll the conditional letters per organisation, then assign each letter:
  - a date (death date + uniform random offset within the catalogue window)
  - an "addressed to" target resolved from the catalogue's `adres_huidig` token
  - a "salutation" rendered from `aanhef_huidig` with placeholders filled
"""

from __future__ import annotations

import random
from datetime import timedelta
from typing import Any

from ._common import BRON, load_yaml, new_uuid
from .brp import OverledeneRecord

# ─────────────────────────────────────────────────────────────────────────────
# Conditional logic for each `voorwaarden` clause (best-effort heuristics)
# ─────────────────────────────────────────────────────────────────────────────


def _record_meets_voorwaarden(
    voorwaarden: list[str],
    *,
    o: OverledeneRecord,
    rng: random.Random,
) -> bool:
    """Approximate evaluation of free-text voorwaarden against the deceased."""
    if not voorwaarden:
        return True

    overledene_age = (o.overlijdensdatum - o.overledene.geboortedatum).days // 365

    for v in voorwaarden:
        v_lower = v.lower()
        if "verzorgingstehuis" in v_lower or "wlz" in v_lower:
            if not o.overledene.woonadres.verzorgingstehuis:
                return False
        elif "aow" in v_lower and overledene_age < 67:
            return False
        elif "voertuig" in v_lower:
            # 50% of deceased ≥ 60 owned a vehicle; ~25% otherwise.
            threshold = 0.50 if overledene_age >= 60 else 0.25
            if rng.random() > threshold:
                return False
        elif "huurtoeslag" in v_lower or "zorgtoeslag" in v_lower:
            # Toeslagen scenarios fire ~55% of the time.
            if rng.random() > 0.55:
                return False
        elif "openstaande boete" in v_lower:
            if rng.random() > 0.10:
                return False
        elif "studieschuld" in v_lower:
            if overledene_age >= 50 or rng.random() > 0.10:
                return False
        elif "eenmanszaak" in v_lower or "wbso" in v_lower or "handelsnaam" in v_lower:
            if rng.random() > 0.10:  # only ~10% are entrepreneurs
                return False
        elif "parkeervergunning" in v_lower:
            if rng.random() > 0.20:
                return False
        elif "ww" in v_lower or "wia" in v_lower:
            if overledene_age >= 67 or rng.random() > 0.05:
                return False
        elif "1 januari" in v_lower or "peildatum" in v_lower:
            # Fires for everyone (the peildatum is always before the death year-end).
            pass
        elif "achterblijvende partner" in v_lower or "partner" in v_lower:
            if o.partner is None:
                return False
        elif "nalatenschap" in v_lower:
            # Most deceased leave at least some estate.
            if rng.random() > 0.85:
                return False
        elif "contactgegevens partner" in v_lower or "contactadres" in v_lower:
            # Only fires if partner exists AND chose to register a contact address.
            if o.partner is None or rng.random() > 0.50:
                return False
        elif "herziene beschikking" in v_lower:
            # Follow-up letters: only if their predecessor fired. Approximate via 50% gate.
            if rng.random() > 0.50:
                return False
        elif "bankrekening" in v_lower:
            if rng.random() > 0.15:
                return False
        elif "openstaand of teveel betaald" in v_lower and rng.random() > 0.30:
            return False
    return True


# ─────────────────────────────────────────────────────────────────────────────
# Address resolution
# ─────────────────────────────────────────────────────────────────────────────


def _resolve_address(token: str, o: OverledeneRecord) -> dict[str, Any]:
    """Map an `adres_huidig` token to a concrete address dict."""
    if token in {
        "woonadres_overledene",
        "laatste_adres_overledene",
        "woonadres_overledene_per_1_januari",
        "vestigingsadres_kvk",
    }:
        return o.overledene.woonadres.to_dict()
    if token == "woonadres_partner":
        if o.partner is not None:
            return o.partner.woonadres.to_dict()
        return o.overledene.woonadres.to_dict()
    if token == "woonadres_overledene_en_ervenadres":
        # Pick the deceased address as the canonical one for this synthetic record.
        return o.overledene.woonadres.to_dict()
    if token == "ervenadres_belastingdienst":
        # In practice this is a Belastingdienst-derived address; in synthetic
        # data we use the partner address if present, else the deceased's.
        if o.partner is not None:
            return o.partner.woonadres.to_dict()
        return o.overledene.woonadres.to_dict()
    if token == "contactadres_partner_indien_bekend":
        if o.partner is not None:
            return o.partner.woonadres.to_dict()
        return o.overledene.woonadres.to_dict()
    # Fallback
    return o.overledene.woonadres.to_dict()


# ─────────────────────────────────────────────────────────────────────────────
# Salutation rendering
# ─────────────────────────────────────────────────────────────────────────────


def _render_aanhef(template: str, o: OverledeneRecord) -> str:
    overledene_naam = f"{o.overledene.voornamen} {o.overledene.geslachtsnaam}"
    partner_naam = (
        f"{o.partner.voornamen} {o.partner.geslachtsnaam}"
        if o.partner is not None
        else overledene_naam
    )
    return (
        template.replace("[naam overledene]", overledene_naam)
        .replace("[overledene]", overledene_naam)
        .replace("[partner]", partner_naam)
        .replace("[handelsnaam]", overledene_naam)
    )


# ─────────────────────────────────────────────────────────────────────────────
# Generator
# ─────────────────────────────────────────────────────────────────────────────


def generate_correspondentie(
    rng: random.Random, overledenen: list[OverledeneRecord]
) -> list[dict[str, Any]]:
    catalogus = load_yaml("brieven-catalogus.yaml")["brieven"]
    out: list[dict[str, Any]] = []

    for o in overledenen:
        for brief in catalogus:
            if not _record_meets_voorwaarden(brief.get("voorwaarden", []), o=o, rng=rng):
                continue

            timing = brief["timing"]
            offset = rng.randint(timing["dag_min"], timing["dag_max"])
            verzonden_op = o.overlijdensdatum + timedelta(days=offset)

            out.append(
                {
                    "id": f"urn:brief:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": o.overledene.bsn,
                    "organisatie": brief["organisatie"],
                    "brief_code": brief["code"],
                    "type": brief["type"],
                    "verzonden_op": verzonden_op.isoformat(),
                    "dagen_na_overlijden": offset,
                    "aanhef": _render_aanhef(brief["aanhef_huidig"], o),
                    "geadresseerde": brief["geadresseerde"],
                    "adres": _resolve_address(brief["adres_huidig"], o),
                    "actie_vereist": brief["actie_vereist"],
                    "actie_omschrijving": brief.get("actie_omschrijving"),
                    "wettelijke_reactietermijn_dagen": brief.get("wettelijke_reactietermijn_dagen"),
                }
            )

    out.sort(key=lambda r: (r["bsn_overledene"], r["verzonden_op"]))
    return out
