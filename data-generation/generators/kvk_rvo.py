"""Layer 6 (optional): KVK / RVO business data of the deceased."""

from __future__ import annotations

import random
from datetime import timedelta
from typing import Any

from ._common import BRON, new_uuid
from .brp import OverledeneRecord

RECHTSVORMEN = [("eenmanszaak", 0.85), ("vof", 0.10), ("bv", 0.05)]
BTW_STATUSSEN = [("actief", 0.70), ("kor", 0.25), ("vrijgesteld", 0.05)]

ONDERNEMER_AANDEEL = 0.10  # ~10% of deceased ran a business


def _weighted(rng: random.Random, items: list[tuple[str, float]]) -> str:
    r = rng.random()
    cumulative = 0.0
    for label, weight in items:
        cumulative += weight
        if r <= cumulative:
            return label
    return items[-1][0]


def generate_kvk_rvo(
    rng: random.Random, overledenen: list[OverledeneRecord]
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for o in overledenen:
        if rng.random() > ONDERNEMER_AANDEEL:
            continue

        kvk_nummer = "".join(str(rng.randint(0, 9)) for _ in range(8))
        suffix = rng.choice(["Advies", "Diensten", "Bouw", "IT", "Werkplaats"])
        handelsnaam = f"{o.overledene.geslachtsnaam} {suffix}"

        wbso = []
        if rng.random() < 0.40:
            looptijd_einde = o.overlijdensdatum + timedelta(days=rng.randint(60, 365))
            wbso.append(
                {
                    "dossiernummer": f"WBSO{rng.randint(100000, 999999)}",
                    "looptijd_einde": looptijd_einde.isoformat(),
                    "uren_te_verantwoorden": rng.randint(40, 600),
                }
            )

        rvo = []
        if rng.random() < 0.30:
            looptijd_einde = o.overlijdensdatum + timedelta(days=rng.randint(90, 720))
            rvo.append(
                {
                    "regeling": rng.choice(["SDE++", "EIA", "MIA/Vamil"]),
                    "dossiernummer": f"RVO{rng.randint(100000, 999999)}",
                    "looptijd_einde": looptijd_einde.isoformat(),
                    "verplichtingen": [
                        "Jaarlijkse voortgangsrapportage",
                        "Eindafrekening bij beëindiging",
                    ],
                }
            )

        out.append(
            {
                "synthetic": True,
                "bron": BRON,
                "bsn_overledene": o.overledene.bsn,
                "kvk_nummer": kvk_nummer,
                "handelsnaam": handelsnaam,
                "rechtsvorm": _weighted(rng, RECHTSVORMEN),
                "btw_status": _weighted(rng, BTW_STATUSSEN),
                "wbso_verplichtingen": wbso,
                "rvo_subsidies": rvo,
            }
        )
        # Avoid unused import warning when generating empty UUIDs unintentionally.
        _ = new_uuid  # keep for potential future use

    return out
