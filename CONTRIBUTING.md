# Contributing

Thanks for your interest in the **OneGov #2 | Inwoner Centraal: Nabestaanden** challenge repository.

This repo is maintained by **GovTech NL / ICTU** for the hackathon on **4–5 June 2026** at The Hague Tech. Contributions are welcome from organisers, mentors, participating teams, and the wider community.

## Ways to contribute

- **Improve documentation**: sharpen personas, legal context, or assessment criteria under [`docs/`](docs/).
- **Extend reference data**: add letter archetypes, organisations, or rates under [`data-generation/reference/`](data-generation/reference/).
- **Refine generators**: tighten the heuristics in [`data-generation/generators/`](data-generation/generators/).
- **Add fixtures**: new golden cases under [`data/fixtures/`](data/fixtures/).
- **Report issues**: use the [issue templates](.github/ISSUE_TEMPLATE/).

## Ground rules

1. **No real personal data.** Every record must be tagged `"synthetic": true` and `"bron": "onegov2-inwoner-centraal-generator"`. BSNs must be 11-proof but otherwise random, never use real ones.
2. **Schemas are the contract.** Changes to [`data/schemas/`](data/schemas/) require a corresponding generator update and a passing test run.
3. **Reproducibility.** All generation must be deterministic given a seed. Avoid wall-clock time, network calls, or non-seeded randomness.
4. **Plain language.** Keep documentation in English (primary) and Dutch where relevant for legal terms.

## Development workflow

```powershell
# Set up
cd data-generation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]

# Regenerate data
python -m generate --seed 42 --n 500 --out ..\data\synthetic

# Run tests + lint
pytest -v
ruff check .
```

CI ([`.github/workflows/validate-data.yml`](.github/workflows/validate-data.yml)) runs the same checks on every push and PR. Please make sure they pass locally before opening a PR.

## Pull requests

- Keep PRs focused, one logical change per PR.
- Update [`README.md`](README.md), schemas, or [`docs/data-dictionary.md`](docs/data-dictionary.md) when behaviour changes.
- Add or extend a fixture if you introduce a new edge case.
- Reference the related issue if there is one.

## Code of Conduct

By participating you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md) (Contributor Covenant 2.1).

## Licensing of contributions

- Code contributions are licensed under **Apache-2.0** (see [`LICENSE`](LICENSE)).
- Data, documentation, and schema contributions are licensed under **CC BY 4.0** (see [`LICENSE-DATA`](LICENSE-DATA)).

By submitting a contribution you confirm that you have the right to license it under these terms.
