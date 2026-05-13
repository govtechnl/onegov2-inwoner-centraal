# API mocks & public sandboxes

> **Why this file exists.** This file curates the public, no-signup-required (or fast-signup) endpoints that map onto the synthetic data layers in [`data/`](../data/), so teams can wire a real-looking API into their demo within an hour.
>
> **Status.** Curated by the organisers. URLs verified at the time of writing - if a sandbox has moved, please open an issue using the [data-issue template](../.github/ISSUE_TEMPLATE/data-issue.md).

## How to use this with the synthetic data

The synthetic JSONL files in [`data/synthetic/`](../data/synthetic/) match the **shape** of the real APIs below as closely as we could without distributing copyrighted schemas. To build a convincing demo:

1. Spin up the sandbox or mock server you need (table below).
2. Replace its sample dataset with our synthetic records (or proxy the call).
3. Build your prototype against the real endpoint signature, not against our JSONL directly.

That way your prototype keeps working when ICTU later swaps the mock for a real connection.

## BRP - Haal Centraal

| Item | Where |
|---|---|
| OpenAPI spec | https://github.com/BRP-API/Haal-Centraal-BRP-bevragen |
| Demo / proefomgeving | https://www.haalcentraal.nl |
| Maps to | [`data/synthetic/overledenen.jsonl`](../data/synthetic/overledenen.jsonl), schema [`01-brp-overlijden.schema.json`](../data/schemas/01-brp-overlijden.schema.json) |
| Useful for | Looking up an `overledene` by BSN, retrieving partner + adres. The "ingeschrevenpersonen" endpoint returns a `overlijden` block. |

## KVK - Handelsregister

| Item | Where |
|---|---|
| Developer portal | https://developers.kvk.nl |
| Test API | https://developers.kvk.nl/documentation/testing |
| Maps to | [`data/synthetic/kvk-rvo.jsonl`](../data/synthetic/kvk-rvo.jsonl), schema [`06-kvk-rvo.schema.json`](../data/schemas/06-kvk-rvo.schema.json) |
| Useful for | Looking up `kvk_nummer` → handelsnaam, rechtsvorm, vestigingsadres for the *Ondernemer* persona. |

## ZGW - Zaken / Documenten / Catalogi (OpenZaak)

| Item | Where |
|---|---|
| Reference impl | https://github.com/open-zaak/open-zaak |
| Public demo | https://demo.openzaak.nl |
| Useful for | Modelling each "verplichting" or "actiebrief" as a *zaak* with status transitions. Lets you demo Common Ground compliance. |

## What to do if a real API is missing

For **ANW intake (SVB)**, **Toeslagen herziening**, **CJIB boete-doorgeven**, **CAK eindafrekening**, **Waterschap aanslag**: no public sandbox exists. Treat these as black-box services and document the request/response contract you'd want them to expose. That documentation is itself a deliverable - see [`docs/beoordelingscriteria.md`](beoordelingscriteria.md).
