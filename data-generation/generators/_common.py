"""Shared helpers: BSN generation, addresses, Faker setup, catalogue loading."""

from __future__ import annotations

import random
import uuid
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml
from faker import Faker

REFERENCE_DIR = Path(__file__).resolve().parent.parent / "reference"

BRON = "onegov2-inwoner-centraal-generator"


def make_faker(seed: int) -> Faker:
    """Create a seeded Dutch Faker."""
    fake = Faker("nl_NL")
    Faker.seed(seed)
    return fake


def make_rng(seed: int) -> random.Random:
    return random.Random(seed)


def load_yaml(name: str) -> Any:
    with (REFERENCE_DIR / name).open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def new_uuid(rng: random.Random) -> str:
    """Deterministic UUID4 from the seeded RNG."""
    return str(uuid.UUID(int=rng.getrandbits(128), version=4))


# ─────────────────────────────────────────────────────────────────────────────
# BSN
# ─────────────────────────────────────────────────────────────────────────────


def generate_bsn(rng: random.Random) -> str:
    """Generate a synthetic 9-digit BSN that passes the 11-proof.

    The 11-proof: sum(d_i * w_i) for i=1..9 with weights 9,8,7,6,5,4,3,2,-1
    must be divisible by 11. We do not start with the digit 0.
    """
    while True:
        digits = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(8)]
        weights = [9, 8, 7, 6, 5, 4, 3, 2, -1]
        if sum(d * w for d, w in zip(digits, weights, strict=True)) % 11 == 0:
            return "".join(str(d) for d in digits)


# ─────────────────────────────────────────────────────────────────────────────
# Addresses
# ─────────────────────────────────────────────────────────────────────────────


@dataclass
class Adres:
    straat: str
    huisnummer: str
    postcode: str
    woonplaats: str
    verzorgingstehuis: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "straat": self.straat,
            "huisnummer": self.huisnummer,
            "postcode": self.postcode,
            "woonplaats": self.woonplaats,
            "verzorgingstehuis": self.verzorgingstehuis,
        }


VERZORGINGSTEHUIZEN = [
    "De Linden",
    "Avondrust",
    "Huize Sint Anna",
    "Het Lindehof",
    "Zorgcentrum De Wilg",
    "Residentie Mariahoeve",
]


def make_address(fake: Faker, rng: random.Random, *, verzorgingstehuis: bool = False) -> Adres:
    straat = fake.street_name() if not verzorgingstehuis else rng.choice(VERZORGINGSTEHUIZEN)
    huisnummer = str(rng.randint(1, 250))
    postcode = f"{rng.randint(1000, 9999)} {chr(rng.randint(65, 90))}{chr(rng.randint(65, 90))}"
    woonplaats = fake.city()
    return Adres(straat, huisnummer, postcode, woonplaats, verzorgingstehuis)


# ─────────────────────────────────────────────────────────────────────────────
# Dates
# ─────────────────────────────────────────────────────────────────────────────


def random_date_between(rng: random.Random, start: date, end: date) -> date:
    delta_days = (end - start).days
    return start + timedelta(days=rng.randint(0, delta_days))


def iso(d: date) -> str:
    return d.isoformat()


# ─────────────────────────────────────────────────────────────────────────────
# Money
# ─────────────────────────────────────────────────────────────────────────────


def euro(amount: float) -> dict[str, str]:
    return {"bedrag": f"{amount:.2f}", "valuta": "EUR"}


# ─────────────────────────────────────────────────────────────────────────────
# JSONL writer
# ─────────────────────────────────────────────────────────────────────────────


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    import json

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_json(path: Path, document: dict[str, Any]) -> None:
    import json

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(document, f, ensure_ascii=False, indent=2)
