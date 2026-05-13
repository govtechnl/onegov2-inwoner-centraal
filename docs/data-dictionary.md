# Data dictionary

This document describes the six data layers (plus optional KVK/RVO layer)
shipped with the challenge. JSON Schemas live in
[`../data/schemas/`](../data/schemas/); generated data lives in
[`../data/synthetic/`](../data/synthetic/); golden persona fixtures live in
[`../data/fixtures/`](../data/fixtures/).

## Conventions across all layers

| Convention | Detail |
|---|---|
| File format | JSON Lines (`.jsonl`) for record sets; JSON for single documents |
| Encoding | UTF-8 |
| Dates | ISO 8601 (`YYYY-MM-DD`) |
| Datetimes | ISO 8601 with timezone (`YYYY-MM-DDTHH:MM:SS+01:00`) |
| Money | Object `{ "bedrag": "123.45", "valuta": "EUR" }` (decimal as string) |
| BSN | 9-digit string. Always paired with `"synthetic": true` at record level. |
| Identifiers | `urn:overlijden:test:<uuid>` style, unambiguous synthetic |
| Language | Field names in Dutch (matching domain), descriptions in English |

> **Synthetic marker.** Every record at the top level carries
> `"synthetic": true` and a `"bron": "onegov2-inwoner-centraal-generator"`
> field. Do not strip these in derivative datasets.

## Layer 1: BRP-style death registration & relationships

**File:** `data/synthetic/overledenen.jsonl`
**Schema:** `data/schemas/01-brp-overlijden.schema.json`
**One record per deceased person.**

| Field | Type | Notes |
|---|---|---|
| `id` | string | Synthetic URN |
| `synthetic` | boolean | Always `true` |
| `overledene.bsn` | string (9) | Synthetic BSN, passes 11-proof |
| `overledene.geslachtsnaam` | string | |
| `overledene.voornamen` | string | |
| `overledene.geboortedatum` | date | |
| `overledene.overlijdensdatum` | date | |
| `overledene.gemeente_overlijden` | string | Gemeente name |
| `overledene.woonadres` | object | Street, postcode, city, *optionally* care home flag |
| `partner.bsn` | string (9) \| null | Null if no surviving partner |
| `partner.geslachtsnaam` | string \| null | |
| `partner.voornamen` | string \| null | |
| `partner.geboortedatum` | date \| null | |
| `partner.woonadres` | object \| null | May differ from `overledene.woonadres` |
| `relatie.vorm` | enum | `huwelijk` \| `geregistreerd_partnerschap` \| `samenwonend` \| `geen` |
| `relatie.aanvang` | date \| null | |

## Layer 2: Outstanding obligations of the deceased

**File:** `data/synthetic/verplichtingen.jsonl`
**Schema:** `data/schemas/02-verplichtingen.schema.json`
**Zero or more records per deceased person.**

| Field | Type | Notes |
|---|---|---|
| `id` | string | Synthetic URN |
| `bsn_overledene` | string (9) | FK to layer 1 |
| `organisatie` | enum | One of the 12 organisations |
| `categorie` | enum | `toeslag` \| `aanslag_ib` \| `erfbelasting` \| `wmo` \| `pensioen` \| `aow` \| `wlz` \| `lokaal_belasting` \| `boete` \| `overig` |
| `omschrijving` | string | Human-readable, e.g. "Zorgtoeslag 2025 - herzien" |
| `bedrag` | money \| null | |
| `peildatum` | date \| null | |
| `vervaldatum` | date \| null | |
| `status` | enum | `open` \| `voldaan` \| `kwijtgescholden` \| `in_behandeling` |
| `wettelijke_termijn_dagen` | integer \| null | |

## Layer 3: Rights of the surviving partner

**File:** `data/synthetic/rechten.jsonl`
**Schema:** `data/schemas/03-rechten-partner.schema.json`
**Zero or more records per surviving partner.**

| Field | Type | Notes |
|---|---|---|
| `id` | string | Synthetic URN |
| `bsn_partner` | string (9) | FK to layer 1 (`partner.bsn`) |
| `organisatie` | enum | |
| `categorie` | enum | `anw` \| `nabestaandenpensioen` \| `toeslag_herberekening` \| `bijstand` \| `inkomensondersteuning` \| `overig` |
| `omschrijving` | string | |
| `geschat_maandbedrag` | money \| null | |
| `voorwaarden` | array of strings | Preconditions in plain language |
| `status` | enum | `mogelijk_recht` \| `toegekend` \| `afgewezen` \| `aanvraag_open` |

## Layer 4: Correspondence stream

**File:** `data/synthetic/correspondentie.jsonl`
**Schema:** `data/schemas/04-correspondentie.schema.json`
**Many records per deceased person - typically 30–80.**

This is the heart of the chaos visualised in
[`casus-truus.md`](casus-truus.md) and
[`../resources/Bijlage-3-correspondentie-nabestaanden.pdf`](../resources/Bijlage-3-correspondentie-nabestaanden.pdf).

| Field | Type | Notes |
|---|---|---|
| `id` | string | |
| `bsn_overledene` | string (9) | FK to layer 1 |
| `organisatie` | enum | |
| `brief_code` | string | Catalogue key from `data-generation/reference/brieven-catalogus.yaml` |
| `type` | enum | `informatiebrief` \| `actiebrief` \| `factuur` \| `aanmaning` \| `condoleance` \| `beschikking` \| `terugvordering` |
| `verzonden_op` | date | Computed from death date + offset |
| `dagen_na_overlijden` | integer | Same offset, exposed for convenience |
| `aanhef` | string | Current state, e.g. "Aan de erven van …" |
| `geadresseerde` | enum | `overledene` \| `erven` \| `partner` \| `contactpersoon` |
| `adres` | object | Where it actually lands today |
| `actie_vereist` | boolean | |
| `actie_omschrijving` | string \| null | |
| `wettelijke_reactietermijn_dagen` | integer \| null | |

## Layer 5: Timeline of expected government actions

**File:** `data/synthetic/tijdlijn.json`
**Schema:** `data/schemas/05-tijdlijn.schema.json`
**One document with an array of expected events per organisation.**

This is a *reference timeline*, independent of any specific deceased person.
Use it to give the bereaved partner predictability: "Expect a letter from
SVB in week 1, a CAK invoice within a month, …"

| Field | Type | Notes |
|---|---|---|
| `organisatie` | enum | |
| `evenementen[].brief_code` | string | |
| `evenementen[].omschrijving` | string | |
| `evenementen[].typische_dag_na_overlijden_min` | integer | |
| `evenementen[].typische_dag_na_overlijden_max` | integer | |
| `evenementen[].voorwaarden` | array of strings | When this event applies |
| `evenementen[].wettelijke_termijn_dagen` | integer \| null | |

## Layer 6: KVK / RVO business data (optional)

**File:** `data/synthetic/kvk-rvo.jsonl`
**Schema:** `data/schemas/06-kvk-rvo.schema.json`
**Records exist for the ~10 % of deceased who ran a business.**

| Field | Type | Notes |
|---|---|---|
| `bsn_overledene` | string (9) | FK to layer 1 |
| `kvk_nummer` | string (8) | Synthetic |
| `handelsnaam` | string | |
| `rechtsvorm` | enum | `eenmanszaak` \| `vof` \| `bv` |
| `btw_status` | enum | `actief` \| `vrijgesteld` \| `kor` |
| `wbso_verplichtingen` | array | Per running WBSO grant |
| `rvo_subsidies` | array | Per running RVO subsidy |

## Provenance

All synthetic data in this repository is generated by the Python tooling in
[`../data-generation/`](../data-generation/). Run:

```pwsh
cd data-generation
python -m generate --seed 42 --n 500 --out ../data/synthetic
```

The seed makes generation reproducible. Catalogue files
(`organisaties.yaml`, `brieven-catalogus.yaml`, `tarieven.yaml`) under
`data-generation/reference/` are the editable source of truth for letter
archetypes, organisation metadata, and amounts.
