"""Validate generated data against the JSON Schemas in `data/schemas/`."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "data" / "schemas"
DATA_GEN = REPO / "data-generation"


@pytest.fixture(scope="session")
def generated_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Generate a small dataset (n=20) into a temp dir for validation."""
    out = tmp_path_factory.mktemp("synthetic")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "generate",
            "--seed",
            "1",
            "--n",
            "20",
            "--out",
            str(out),
        ],
        check=True,
        cwd=DATA_GEN,
    )
    return out


def _load_schema(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((SCHEMAS / name).read_text(encoding="utf-8")))


def _iter_jsonl(path: Path):
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


@pytest.mark.parametrize(
    "filename, schema_name",
    [
        ("overledenen.jsonl", "01-brp-overlijden.schema.json"),
        ("verplichtingen.jsonl", "02-verplichtingen.schema.json"),
        ("rechten.jsonl", "03-rechten-partner.schema.json"),
        ("correspondentie.jsonl", "04-correspondentie.schema.json"),
        ("kvk-rvo.jsonl", "06-kvk-rvo.schema.json"),
    ],
)
def test_jsonl_layer_validates(generated_dir: Path, filename: str, schema_name: str) -> None:
    validator = _load_schema(schema_name)
    path = generated_dir / filename
    assert path.exists(), f"Generator did not produce {filename}"
    for record in _iter_jsonl(path):
        errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
        assert not errors, (
            f"Schema validation failed for {filename}: "
            + "; ".join(e.message for e in errors[:3])
        )


def test_tijdlijn_validates(generated_dir: Path) -> None:
    validator = _load_schema("05-tijdlijn.schema.json")
    document = json.loads((generated_dir / "tijdlijn.json").read_text(encoding="utf-8"))
    errors = sorted(validator.iter_errors(document), key=lambda e: e.path)
    assert not errors, "Schema validation failed for tijdlijn.json: " + "; ".join(
        e.message for e in errors[:3]
    )


def test_correspondentie_references_existing_overledenen(generated_dir: Path) -> None:
    """Every brief.bsn_overledene must exist in the BRP layer."""
    bsns = {r["overledene"]["bsn"] for r in _iter_jsonl(generated_dir / "overledenen.jsonl")}
    for r in _iter_jsonl(generated_dir / "correspondentie.jsonl"):
        assert r["bsn_overledene"] in bsns
