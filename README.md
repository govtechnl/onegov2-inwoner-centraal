# OneGov #2 | Inwoner Centraal: Nabestaanden

> *From chaos to control: one government overview for bereaved partners.*

This repository hosts the challenge brief, supporting documents, synthetic
datasets, and data-generation tooling for the second **OneGov** hackathon,
hosted by [GovTech NL](https://govtechnl.nl) and challenge owner
[ICTU](https://www.ictu.nl).

- **Theme:** Inwoner Centraal (Citizen-centric)
- **Date:** 4–5 June 2026
- **Location:** The Hague Tech, Den Haag
- **Challenge owners:** Natalie Moreno Robles & Ingrid Verhage (ICTU)
- **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)

## The challenge in one paragraph

When someone loses a partner, they enter one of the hardest periods of their
life - and an administrative storm. Bereaved partners receive correspondence
from up to **twelve different government organisations** (Gemeente, SVB, CAK,
RDW, Waterschap, Belastingdienst, Toeslagen, RVO, CJIB, UWV, DUO, KVK), each
operating from its own silo. The same data is requested over and over while
the *doenvermogen* (capacity to act under emotional pressure) is at its lowest.

**How can we help bereaved partners get a complete, proactive, personalised
view of their rights and obligations across the entire government - without
making them chase it themselves?**

The full brief is in [CHALLENGE.md](CHALLENGE.md).

New teams can begin with [START_HERE.md](START_HERE.md).

## Two tracks

Teams pick one (or show how they connect):

1. **Stap 1: De gebundelde eerste brief.** A single, empathic letter on
   behalf of the whole government, sent shortly after the death.
2. **Stap 2: Het gepersonaliseerde totaaloverzicht.** A digital "loket" where
   the bereaved sees every running obligation and right at a glance.

## Repository layout

| Path | Purpose |
|---|---|
| [CHALLENGE.md](CHALLENGE.md) | Full challenge brief (English translation of the Dutch original) |
| [docs/](docs/) | Personas, the Truus & Cees case, legal context, judging criteria, architecture notes |
| [resources/](resources/) | Original source materials (DOCX, PPTX, PDF) provided by ICTU |
| [data/schemas/](data/schemas/) | JSON Schemas for every data layer |
| [data/synthetic/](data/synthetic/) | Generated synthetic datasets (output of the generator) |
| [data/fixtures/](data/fixtures/) | Hand-curated golden cases matching each persona |
| [data-generation/](data-generation/) | Python tooling that generates the synthetic data |

## Quick start: generate the data

```pwsh
cd data-generation
uv venv             # or: python -m venv .venv
uv pip install -e .
python -m generate --seed 42 --n 500 --out ../data/synthetic
```

The generator produces six data layers (BRP-style death registration,
outstanding obligations, partner rights, correspondence stream, expected
timeline, and optional KVK/RVO business data) plus four hand-curated fixtures
that mirror the personas.

See [data/README.md](data/README.md) for the data dictionary and provenance.

## Disclaimer

All data in this repository is **fully synthetic** and contains no personal
data of real citizens. BSN-like identifiers are generated for testing and are
explicitly tagged with a `"synthetic": true` marker. Prototypes built during
the hackathon are **not policy commitments** and require further review before
any production use.

## Licensing

- **Code** is released under the [Apache License 2.0](LICENSE).
- **Data, documentation, and challenge text** are released under
  [CC BY 4.0](LICENSE-DATA).

## Contributing

Issues and pull requests are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).
