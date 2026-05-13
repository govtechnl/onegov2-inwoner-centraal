# `data/` - synthetic datasets

> **Synthetic only.** No personal data of real citizens. All BSNs are
> generated for testing and tagged with `"synthetic": true`.

This folder ships in three subdirectories:

- [`schemas/`](schemas/) - JSON Schema (Draft 2020-12) for every data layer.
- [`synthetic/`](synthetic/) - generated bulk datasets (run the generator to
  populate; placeholders may be checked in).
- [`fixtures/`](fixtures/) - hand-curated "golden" cases that match each
  persona one-to-one.

For the field-by-field documentation see
[`../docs/data-dictionary.md`](../docs/data-dictionary.md).

## Layers at a glance

| # | Layer | File | Records | Schema |
|---|---|---|---|---|
| 1 | BRP-style death registration & relationships | `synthetic/overledenen.jsonl` | one per deceased | [01-brp-overlijden.schema.json](schemas/01-brp-overlijden.schema.json) |
| 2 | Outstanding obligations of the deceased | `synthetic/verplichtingen.jsonl` | many per deceased | [02-verplichtingen.schema.json](schemas/02-verplichtingen.schema.json) |
| 3 | Rights of the surviving partner | `synthetic/rechten.jsonl` | many per partner | [03-rechten-partner.schema.json](schemas/03-rechten-partner.schema.json) |
| 4 | Correspondence stream | `synthetic/correspondentie.jsonl` | 30–80 per deceased | [04-correspondentie.schema.json](schemas/04-correspondentie.schema.json) |
| 5 | Reference timeline of expected actions | `synthetic/tijdlijn.json` | one document | [05-tijdlijn.schema.json](schemas/05-tijdlijn.schema.json) |
| 6 | KVK / RVO business data (optional) | `synthetic/kvk-rvo.jsonl` | ~10 % of deceased | [06-kvk-rvo.schema.json](schemas/06-kvk-rvo.schema.json) |

## Generating the data

```pwsh
cd ..\data-generation
python -m generate --seed 42 --n 500 --out ..\data\synthetic
```

The generator is deterministic: same `--seed` ⇒ identical output. Default
size is 500 deceased persons; raise `--n` for stress tests.

## Fixtures

Four hand-curated cases mirror the personas in
[`../docs/personas.md`](../docs/personas.md):

| Fixture | Persona | What it exercises |
|---|---|---|
| [`fixtures/truus-cees.json`](fixtures/truus-cees.json) | Truus, 62 | Full letter inventory of [`../docs/casus-truus.md`](../docs/casus-truus.md) |
| [`fixtures/marcus.json`](fixtures/marcus.json) | Marcus, 48 | Locked-out partner, *nabestaanden­machtiging* needed |
| [`fixtures/anneke.json`](fixtures/anneke.json) | Anneke, 71 | Low digital skill, language sensitivity |
| [`fixtures/ondernemer.json`](fixtures/ondernemer.json) | Bereaved entrepreneur | Layer 6 (KVK/RVO) populated |

Use the fixtures as the demo cases for your jury pitch - they are stable
across runs and small enough to walk through on screen.

## Validating

```pwsh
cd ..\data-generation
python -m pytest
```

CI ([`/.github/workflows/validate-data.yml`](../.github/workflows/validate-data.yml))
runs the same validation on every push.
