# `data-generation/`

Python tooling that generates the synthetic datasets in
[`../data/synthetic/`](../data/synthetic/).

## Install

Using [uv](https://docs.astral.sh/uv/) (recommended):

```pwsh
uv venv
uv pip install -e .[dev]
```

Or with stock Python:

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

## Generate

```pwsh
python -m generate --seed 42 --n 500 --out ..\data\synthetic
```

Options:

| Flag | Default | Meaning |
|---|---|---|
| `--seed` | `42` | RNG seed; same seed ⇒ identical output |
| `--n` | `500` | Number of deceased persons |
| `--out` | `../data/synthetic` | Output directory |
| `--start-date` | `2025-01-01` | Earliest synthetic date of death |
| `--end-date` | `2025-12-31` | Latest synthetic date of death |

## Layout

```
data-generation/
├── generate.py              # CLI entrypoint
├── generators/
│   ├── __init__.py
│   ├── _common.py           # BSN, dates, addresses, Faker setup
│   ├── brp.py               # layer 1
│   ├── verplichtingen.py    # layer 2
│   ├── rechten.py           # layer 3
│   ├── correspondentie.py   # layer 4
│   ├── tijdlijn.py          # layer 5
│   └── kvk_rvo.py           # layer 6 (optional)
├── reference/
│   ├── organisaties.yaml
│   ├── brieven-catalogus.yaml
│   └── tarieven.yaml
└── tests/
    └── test_schemas.py      # validate generated output against JSON Schemas
```

## Tests

```pwsh
python -m pytest
```

The schema-validation tests regenerate a small sample (n=20) and validate
every record against the JSON Schemas under
[`../data/schemas/`](../data/schemas/).
