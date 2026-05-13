"""Layer 1: BRP-style death registration & relationships."""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any

from faker import Faker

from ._common import (
    BRON,
    Adres,
    generate_bsn,
    iso,
    make_address,
    new_uuid,
    random_date_between,
)


@dataclass
class Persoon:
    bsn: str
    geslachtsnaam: str
    voornamen: str
    geboortedatum: date
    woonadres: Adres


@dataclass
class OverledeneRecord:
    id: str
    overledene: Persoon
    overlijdensdatum: date
    gemeente_overlijden: str
    partner: Persoon | None
    relatie_vorm: str
    relatie_aanvang: date | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "synthetic": True,
            "bron": BRON,
            "overledene": {
                "bsn": self.overledene.bsn,
                "geslachtsnaam": self.overledene.geslachtsnaam,
                "voornamen": self.overledene.voornamen,
                "geboortedatum": iso(self.overledene.geboortedatum),
                "overlijdensdatum": iso(self.overlijdensdatum),
                "gemeente_overlijden": self.gemeente_overlijden,
                "woonadres": self.overledene.woonadres.to_dict(),
            },
            "partner": (
                None
                if self.partner is None
                else {
                    "bsn": self.partner.bsn,
                    "geslachtsnaam": self.partner.geslachtsnaam,
                    "voornamen": self.partner.voornamen,
                    "geboortedatum": iso(self.partner.geboortedatum),
                    "woonadres": self.partner.woonadres.to_dict(),
                }
            ),
            "relatie": {
                "vorm": self.relatie_vorm,
                "aanvang": iso(self.relatie_aanvang) if self.relatie_aanvang else None,
            },
        }


# Approximate distribution: weighted toward older deaths (CBS sterftecijfers).
AGE_AT_DEATH_BUCKETS = [
    (45, 60, 0.07),
    (60, 70, 0.13),
    (70, 80, 0.27),
    (80, 90, 0.36),
    (90, 100, 0.17),
]

RELATIE_DISTRIBUTIE = [
    ("huwelijk", 0.55),
    ("geregistreerd_partnerschap", 0.05),
    ("samenwonend", 0.20),
    ("geen", 0.20),
]


def _weighted_choice(rng: random.Random, items: list[tuple]) -> tuple:
    r = rng.random()
    cumulative = 0.0
    for item in items:
        cumulative += item[-1]
        if r <= cumulative:
            return item
    return items[-1]


def _random_age_at_death(rng: random.Random) -> int:
    bucket = _weighted_choice(rng, AGE_AT_DEATH_BUCKETS)
    return rng.randint(bucket[0], bucket[1] - 1)


def _random_relatie_vorm(rng: random.Random) -> str:
    return _weighted_choice(rng, RELATIE_DISTRIBUTIE)[0]


def make_persoon(
    fake: Faker,
    rng: random.Random,
    *,
    geboortedatum: date,
    geslacht: str | None = None,
    woonadres: Adres | None = None,
) -> Persoon:
    if geslacht is None:
        geslacht = "male" if rng.random() < 0.5 else "female"
    voornamen = fake.first_name_male() if geslacht == "male" else fake.first_name_female()
    geslachtsnaam = fake.last_name()
    if woonadres is None:
        woonadres = make_address(fake, rng)
    return Persoon(
        bsn=generate_bsn(rng),
        geslachtsnaam=geslachtsnaam,
        voornamen=voornamen,
        geboortedatum=geboortedatum,
        woonadres=woonadres,
    )


def generate_overledenen(
    fake: Faker,
    rng: random.Random,
    *,
    n: int,
    start_date: date,
    end_date: date,
) -> list[OverledeneRecord]:
    records: list[OverledeneRecord] = []
    for _ in range(n):
        overlijdensdatum = random_date_between(rng, start_date, end_date)
        leeftijd = _random_age_at_death(rng)
        geboortedatum = overlijdensdatum - timedelta(days=leeftijd * 365 + rng.randint(-180, 180))

        # Probability the deceased lived in a care home, increases sharply with age.
        in_verzorgingstehuis = rng.random() < (0.05 if leeftijd < 75 else 0.30)
        woonadres_overledene = make_address(fake, rng, verzorgingstehuis=in_verzorgingstehuis)

        overledene = make_persoon(
            fake, rng, geboortedatum=geboortedatum, woonadres=woonadres_overledene
        )

        relatie_vorm = _random_relatie_vorm(rng)
        partner: Persoon | None = None
        relatie_aanvang: date | None = None

        if relatie_vorm != "geen":
            # Partner usually within ±10 years; if deceased lived in a care home,
            # the partner often still lives in their joint home (different address).
            partner_leeftijd = max(40, leeftijd + rng.randint(-10, 10))
            partner_geboortedatum = overlijdensdatum - timedelta(
                days=partner_leeftijd * 365 + rng.randint(-180, 180)
            )
            partner_woonadres = (
                make_address(fake, rng, verzorgingstehuis=False)
                if in_verzorgingstehuis
                else woonadres_overledene
            )
            partner = make_persoon(
                fake,
                rng,
                geboortedatum=partner_geboortedatum,
                woonadres=partner_woonadres,
            )
            # Relationship duration 5-50 years.
            relatie_aanvang = overlijdensdatum - timedelta(days=rng.randint(5, 50) * 365)

        records.append(
            OverledeneRecord(
                id=f"urn:overlijden:test:{new_uuid(rng)}",
                overledene=overledene,
                overlijdensdatum=overlijdensdatum,
                gemeente_overlijden=fake.city(),
                partner=partner,
                relatie_vorm=relatie_vorm,
                relatie_aanvang=relatie_aanvang,
            )
        )
    return records
