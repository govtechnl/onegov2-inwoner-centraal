"""Layer 3: rights of the surviving partner."""

from __future__ import annotations

import random
from typing import Any

from ._common import BRON, euro, load_yaml, new_uuid
from .brp import OverledeneRecord

AOW_LEEFTIJD = 67  # benadering


def generate_rechten(
    rng: random.Random, overledenen: list[OverledeneRecord]
) -> list[dict[str, Any]]:
    tarieven = load_yaml("tarieven.yaml")
    out: list[dict[str, Any]] = []

    for o in overledenen:
        if o.partner is None:
            continue

        d = o.overlijdensdatum
        partner = o.partner
        partner_age = (d - partner.geboortedatum).days // 365
        bsn_partner = partner.bsn

        # ─── ANW (alleen onder AOW-leeftijd, met voorwaarden) ─────────────────
        if partner_age < AOW_LEEFTIJD and rng.random() < 0.55:
            out.append(
                {
                    "id": f"urn:recht:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_partner": bsn_partner,
                    "organisatie": "SVB",
                    "categorie": "anw",
                    "omschrijving": "ANW-uitkering nabestaande",
                    "geschat_maandbedrag": euro(float(tarieven["anw"]["bruto_per_maand_basis"])),
                    "voorwaarden": [
                        "Geboren voor 1950, of zorg voor kind onder 18, "
                        "of arbeidsongeschikt voor minimaal 45%",
                        "Inkomen onder grensbedrag",
                    ],
                    "status": "mogelijk_recht",
                }
            )

        # ─── Overlijdensuitkering AOW (1 maand AOW + vakantiegeld) ───────────
        # Geldt alleen als overledene AOW ontving — proxy: leeftijd ≥ AOW
        overledene_age = (d - o.overledene.geboortedatum).days // 365
        if overledene_age >= AOW_LEEFTIJD:
            out.append(
                {
                    "id": f"urn:recht:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_partner": bsn_partner,
                    "organisatie": "SVB",
                    "categorie": "overig",
                    "omschrijving": "Overlijdensuitkering AOW (1 maand AOW + vakantiegeld)",
                    "geschat_maandbedrag": euro(
                        float(tarieven["aow"]["bruto_per_maand_gehuwd"])
                        + float(tarieven["aow"]["vakantiegeld_jaarlijks"]) / 12
                    ),
                    "voorwaarden": ["Overledene ontving AOW", "Achterblijvende partner"],
                    "status": "toegekend",
                }
            )

        # ─── Toeslag-herberekening (huurtoeslag/zorgtoeslag) ─────────────────
        if rng.random() < 0.45:
            out.append(
                {
                    "id": f"urn:recht:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_partner": bsn_partner,
                    "organisatie": "Toeslagen",
                    "categorie": "toeslag_herberekening",
                    "omschrijving": "Herberekening toeslagen op basis van nieuw huishoudinkomen",
                    "geschat_maandbedrag": None,
                    "voorwaarden": [
                        "Inkomenswijziging na overlijden partner",
                        "Toeslag wordt opnieuw berekend vanaf maand na overlijden",
                    ],
                    "status": "aanvraag_open",
                }
            )

        # ─── Nabestaandenpensioen (proxy via werknemerspensioen-flag) ─────────
        if rng.random() < 0.35:
            out.append(
                {
                    "id": f"urn:recht:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_partner": bsn_partner,
                    "organisatie": "UWV",  # placeholder — feitelijk pensioenfonds
                    "categorie": "nabestaandenpensioen",
                    "omschrijving": "Nabestaandenpensioen via pensioenfonds",
                    "geschat_maandbedrag": euro(round(rng.uniform(200, 1500), 2)),
                    "voorwaarden": [
                        "Overledene was deelnemer aan pensioenregeling",
                        "Regeling kent partnerpensioen",
                    ],
                    "status": "mogelijk_recht",
                }
            )

        # ─── Bijstand / inkomensondersteuning (alleen bij sterke inkomensdaling) ───
        if partner_age < AOW_LEEFTIJD and rng.random() < 0.10:
            out.append(
                {
                    "id": f"urn:recht:test:{new_uuid(rng)}",
                    "synthetic": True,
                    "bron": BRON,
                    "bsn_partner": bsn_partner,
                    "organisatie": "Gemeente",
                    "categorie": "bijstand",
                    "omschrijving": "Mogelijk recht op bijstand bij inkomensterugval",
                    "geschat_maandbedrag": None,
                    "voorwaarden": [
                        "Inkomen onder bijstandsnorm",
                        "Geen recht op andere voorliggende voorzieningen",
                    ],
                    "status": "mogelijk_recht",
                }
            )

    return out
