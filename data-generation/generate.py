"""CLI entrypoint: regenerate every synthetic data layer reproducibly.

Usage:

    python -m generate --seed 42 --n 500 --out ../data/synthetic
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from generators._common import make_faker, make_rng, write_json, write_jsonl
from generators.brp import generate_overledenen
from generators.correspondentie import generate_correspondentie
from generators.kvk_rvo import generate_kvk_rvo
from generators.rechten import generate_rechten
from generators.tijdlijn import generate_tijdlijn
from generators.verplichtingen import generate_verplichtingen


def _parse_date(s: str) -> date:
    return date.fromisoformat(s)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate synthetic datasets for the OneGov #2 Nabestaanden challenge."
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n", type=int, default=500, help="Number of deceased persons")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data" / "synthetic",
    )
    parser.add_argument("--start-date", type=_parse_date, default=date(2025, 1, 1))
    parser.add_argument("--end-date", type=_parse_date, default=date(2025, 12, 31))
    args = parser.parse_args()

    out: Path = args.out
    fake = make_faker(args.seed)
    rng = make_rng(args.seed)

    print(f"[1/6] Generating {args.n} deceased persons (BRP layer)…")
    overledenen = generate_overledenen(
        fake, rng, n=args.n, start_date=args.start_date, end_date=args.end_date
    )
    write_jsonl(out / "overledenen.jsonl", [o.to_dict() for o in overledenen])

    print("[2/6] Generating outstanding obligations…")
    write_jsonl(out / "verplichtingen.jsonl", generate_verplichtingen(rng, overledenen))

    print("[3/6] Generating partner rights…")
    write_jsonl(out / "rechten.jsonl", generate_rechten(rng, overledenen))

    print("[4/6] Generating correspondence stream…")
    write_jsonl(out / "correspondentie.jsonl", generate_correspondentie(rng, overledenen))

    print("[5/6] Generating reference timeline…")
    write_json(out / "tijdlijn.json", generate_tijdlijn())

    print("[6/6] Generating KVK / RVO business data…")
    write_jsonl(out / "kvk-rvo.jsonl", generate_kvk_rvo(rng, overledenen))

    print(f"\nDone. Output written to {out.resolve()}")


if __name__ == "__main__":
    main()
