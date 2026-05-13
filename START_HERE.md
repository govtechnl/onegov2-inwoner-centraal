# Start Here (Hackathon Teams)

If you are starting this challenge now, use this order.

## 1) Read the challenge scope (10 min)

- Read [CHALLENGE.md](CHALLENGE.md).
- Skim [docs/beoordelingscriteria.md](docs/beoordelingscriteria.md).
- Read the Truus & Cees case in [docs/casus-truus.md](docs/casus-truus.md).

## 2) Pick your track (5 min)

- Track 1: bundled first letter.
- Track 2: personalized total overview.
- Hybrid: do a minimal end-to-end flow covering both.

## 3) Generate synthetic data (15 min)

```powershell
cd data-generation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
python -m generate --seed 42 --n 500 --out ..\data\synthetic
```

## 4) Inspect the data model (10 min)

- Schemas: [data/schemas/](data/schemas/)
- Synthetic output: [data/synthetic/](data/synthetic/)
- Golden fixtures: [data/fixtures/](data/fixtures/)
- Data dictionary: [data/README.md](data/README.md)

## 5) Build your prototype slice

- Start from one persona/scenario.
- Keep data usage synthetic and reproducible.
- Document assumptions in your PR and pitch.

## 6) Before submission

- Validate against judging criteria.
- Include what works, what is incomplete, and next steps.
- Keep one PR per team.