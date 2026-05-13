"""Layer 5: reference timeline of expected government actions.

Derived directly from the letter catalogue. One document; one entry per
organisation; events grouped under that organisation.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._common import BRON, load_yaml


def generate_tijdlijn() -> dict[str, Any]:
    catalogus = load_yaml("brieven-catalogus.yaml")["brieven"]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for brief in catalogus:
        grouped[brief["organisatie"]].append(
            {
                "brief_code": brief["code"],
                "omschrijving": brief["omschrijving"],
                "typische_dag_na_overlijden_min": brief["timing"]["dag_min"],
                "typische_dag_na_overlijden_max": brief["timing"]["dag_max"],
                "voorwaarden": brief.get("voorwaarden", []),
                "wettelijke_termijn_dagen": brief.get("wettelijke_reactietermijn_dagen"),
            }
        )

    organisaties = sorted(grouped.keys())
    for org in organisaties:
        grouped[org].sort(key=lambda e: e["typische_dag_na_overlijden_min"])

    return {
        "synthetic": True,
        "bron": BRON,
        "organisaties": [
            {"organisatie": org, "evenementen": grouped[org]} for org in organisaties
        ],
    }
