"""Layer 2: outstanding obligations of the deceased."""

from __future__ import annotations

import random
from datetime import date, timedelta
from typing import Any

from ._common import BRON, euro, iso, load_yaml, new_uuid
from .brp import OverledeneRecord


def _money_in_range(rng: random.Random, lo: str, hi: str) -> dict[str, str]:
    return euro(round(rng.uniform(float(lo), float(hi)), 2))


def generate_verplichtingen(
    rng: random.Random, overledenen: list[OverledeneRecord]
) -> list[dict[str, Any]]:
    tarieven = load_yaml("tarieven.yaml")
    out: list[dict[str, Any]] = []

    for o in overledenen:
        d = o.overlijdensdatum
        bsn = o.overledene.bsn

        # ─── Toeslagen herziening (zorgtoeslag) — most common ────────────────
        if rng.random() < 0.55:
            terug = round(rng.uniform(50, 600), 2)
            out.append(
                {
                    "id": f"urn:verplichting:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": bsn,
                    "organisatie": "Toeslagen",
                    "categorie": "toeslag",
                    "omschrijving": "Terugvordering zorgtoeslag na herziening",
                    "bedrag": euro(terug),
                    "peildatum": iso(d.replace(month=1, day=1)),
                    "vervaldatum": iso(d + timedelta(days=42)),
                    "status": "open",
                    "wettelijke_termijn_dagen": 42,
                }
            )

        # ─── Erfbelasting (8 maanden termijn) ────────────────────────────────
        if rng.random() < 0.45:
            erf = round(rng.uniform(0, 35000), 2)
            out.append(
                {
                    "id": f"urn:verplichting:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": bsn,
                    "organisatie": "Belastingdienst",
                    "categorie": "erfbelasting",
                    "omschrijving": "Aangifte erfbelasting",
                    "bedrag": euro(erf) if erf > 0 else None,
                    "peildatum": iso(d),
                    "vervaldatum": iso(d + timedelta(days=240)),
                    "status": "open",
                    "wettelijke_termijn_dagen": 240,
                }
            )

        # ─── WLZ-eigen bijdrage (alleen indien verzorgingstehuis) ────────────
        if o.overledene.woonadres.verzorgingstehuis:
            wlz = _money_in_range(
                rng,
                tarieven["wlz_eigen_bijdrage"]["per_maand_min"],
                tarieven["wlz_eigen_bijdrage"]["per_maand_max"],
            )
            out.append(
                {
                    "id": f"urn:verplichting:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": bsn,
                    "organisatie": "CAK",
                    "categorie": "wlz",
                    "omschrijving": "WLZ-eigen bijdrage (laatste maand)",
                    "bedrag": wlz,
                    "peildatum": iso(d),
                    "vervaldatum": iso(d + timedelta(days=30)),
                    "status": "open",
                    "wettelijke_termijn_dagen": 30,
                }
            )

        # ─── Waterschapsbelasting (peildatum 1 jan) ──────────────────────────
        if rng.random() < 0.40:
            ws = _money_in_range(
                rng,
                tarieven["waterschapsbelasting"]["per_huishouden_per_jaar_min"],
                tarieven["waterschapsbelasting"]["per_huishouden_per_jaar_max"],
            )
            out.append(
                {
                    "id": f"urn:verplichting:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": bsn,
                    "organisatie": "Waterschap",
                    "categorie": "lokaal_belasting",
                    "omschrijving": "Waterschapsbelasting (peildatum 1 januari)",
                    "bedrag": ws,
                    "peildatum": iso(date(d.year, 1, 1)),
                    "vervaldatum": iso(d + timedelta(days=60)),
                    "status": "open",
                    "wettelijke_termijn_dagen": 42,
                }
            )

        # ─── Aanslag IB overlijdensjaar ──────────────────────────────────────
        if rng.random() < 0.30:
            ib = round(rng.uniform(-500, 1500), 2)
            out.append(
                {
                    "id": f"urn:verplichting:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": bsn,
                    "organisatie": "Belastingdienst",
                    "categorie": "aanslag_ib",
                    "omschrijving": "Aanslag IB overlijdensjaar",
                    "bedrag": euro(ib),
                    "peildatum": iso(d),
                    "vervaldatum": iso(d + timedelta(days=365)),
                    "status": "open",
                    "wettelijke_termijn_dagen": 42,
                }
            )

        # ─── CJIB openstaande boete ──────────────────────────────────────────
        if rng.random() < 0.10:
            boete = _money_in_range(
                rng,
                tarieven["cjib_boete"]["bedrag_min"],
                tarieven["cjib_boete"]["bedrag_max"],
            )
            out.append(
                {
                    "id": f"urn:verplichting:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_overledene": bsn,
                    "organisatie": "CJIB",
                    "categorie": "boete",
                    "omschrijving": "Openstaande boete",
                    "bedrag": boete,
                    "peildatum": iso(d - timedelta(days=rng.randint(7, 90))),
                    "vervaldatum": iso(d + timedelta(days=42)),
                    "status": "open",
                    "wettelijke_termijn_dagen": 42,
                }
            )

    return out
