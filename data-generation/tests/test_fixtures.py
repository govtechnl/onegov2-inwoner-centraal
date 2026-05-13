"""Validate the hand-curated golden fixtures against the JSON Schemas."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "data" / "schemas"
FIXTURES = REPO / "data" / "fixtures"


def _validator(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((SCHEMAS / name).read_text(encoding="utf-8")))


@pytest.fixture(scope="session")
def validators() -> dict[str, Draft202012Validator]:
    return {
        "overledene": _validator("01-brp-overlijden.schema.json"),
        "verplichting": _validator("02-verplichtingen.schema.json"),
        "recht": _validator("03-rechten-partner.schema.json"),
        "brief": _validator("04-correspondentie.schema.json"),
        "kvk_rvo": _validator("06-kvk-rvo.schema.json"),
    }


@pytest.mark.parametrize(
    "fixture", ["truus-cees.json", "marcus.json", "anneke.json", "ondernemer.json"]
)
def test_fixture_validates(validators, fixture: str) -> None:
    doc = json.loads((FIXTURES / fixture).read_text(encoding="utf-8"))

    def _check(record, validator, label):
        errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
        assert not errors, f"{fixture} {label}: {'; '.join(e.message for e in errors[:3])}"

    _check(doc["overledene"], validators["overledene"], "overledene")
    for r in doc.get("verplichtingen", []):
        _check(r, validators["verplichting"], "verplichting")
    for r in doc.get("rechten", []):
        _check(r, validators["recht"], "recht")
    for r in doc.get("correspondentie", []):
        _check(r, validators["brief"], "brief")
    if doc.get("kvk_rvo"):
        _check(doc["kvk_rvo"], validators["kvk_rvo"], "kvk_rvo")
