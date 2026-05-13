# Architecture context: building blocks to reason from

This document maps the existing landscape your prototype should *plug into*
rather than replace. The jury rewards solutions that reason from existing
building blocks - see [`beoordelingscriteria.md`](beoordelingscriteria.md).

## The 12 organisations in scope

| # | Organisation | Role | Key data | Channel today |
|---|---|---|---|---|
| 1 | **Gemeente** | Registers death in BRP, condolences, parking permits, local taxes | Address, marital status, gemeentelijke belastingen | Letter + own portal |
| 2 | **SVB** | AOW, ANW, *overlijdens­uitkering* | Pension status, ANW eligibility | Mijn SVB + letter |
| 3 | **CAK** | WLZ contributions | WLZ invoices | Letter + own portal |
| 4 | **RDW** | Vehicle registration | Tenaamstelling, transfer obligations | Letter |
| 5 | **Waterschap** | Water-system & purification levies | Annual assessment | Letter |
| 6 | **Belastingdienst** | Income tax, inheritance tax | IB assessments, *erfbelasting* | Berichtenbox + letter |
| 7 | **Toeslagen** | Zorg-, huur-, kindgebonden-, kinderopvang­toeslag | Toeslag entitlements & recoveries | Berichtenbox + letter |
| 8 | **RVO** | Subsidies (incl. WBSO) for entrepreneurs | Subsidy obligations | Mijn RVO + letter |
| 9 | **CJIB** | Collection (fines, incasso) | Outstanding fines, payment terms | Letter |
| 10 | **UWV** | Employee insurance | WW, WIA status | Mijn UWV + letter |
| 11 | **DUO** | Student finance | Study debt | Mijn DUO + letter |
| 12 | **KVK** | Business registry (*Handelsregister*) | KVK registration, business address | Letter + KVK portal |

## Existing building blocks you can lean on

### Identity & authorisation

- **DigiD**: citizen identity. Lapses on death.
- **eHerkenning**: business identity.
- **Machtigen** ([machtigen.digid.nl](https://machtigen.digid.nl)): Logius
  authorisation service. The natural home for a *nabestaanden­machtiging*.

### Communication channels

- **MijnOverheid** ([mijn.overheid.nl](https://mijn.overheid.nl)): citizen
  portal aggregating data from base registries and offering the
  Berichtenbox.
- **Berichtenbox**: official digital mailbox. Opt-in. Carries messages from
  Belastingdienst, SVB, RDW, gemeenten, and others.
- **Notify NL** ([github.com/MinBZK/notify-nl](https://github.com/MinBZK/notify-nl)):
  outbound notification service modelled on UK Notify.

### Data infrastructure

- **Haal Centraal BRP API**: modern REST read-API on BRP. Already used by
  multiple uitvoerings­organisaties.
- **Stelselcatalogus** ([stelselcatalogus.nl](https://www.stelselcatalogus.nl)):
  catalogue of definitions across the base registries.
- **Common Ground** ([commonground.nl](https://commonground.nl)): separate
  data, services, and applications. Consume registries; don't copy them.
- **NL API Strategie** ([developer.overheid.nl](https://developer.overheid.nl)):
  REST conventions, OAS profiles, ADRs.
- **Digikoppeling / Digipoort**: secure G2G messaging.

### Service-design references

- **Aanpak Levensgebeurtenissen** (BZK): multidisciplinary approach to
  life-event services. Has produced the inventory of letter flows that
  underpins this challenge.
- **Programma Mens Centraal**: research and design programme that produced
  the persona research used in this challenge.
- **rijksoverheid.nl/overlijden**: current central content page for
  bereavement.

## A reference architecture sketch for the bundled overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      Bereaved partner                           │
│   (web, app, post, telephone, channel of their choice)         │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                    "One government" frontend                    │
│   - Personalised overview (rights + obligations)                │
│   - Bundled first letter generator                              │
│   - Defer / correct / contact actions                           │
└────────────────────────────────┬────────────────────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
       ┌──────────────┐  ┌──────────────┐   ┌──────────────┐
       │  Aggregator  │  │   Machtigen  │   │   Notify /   │
       │   service    │  │  (delegated  │   │  Berichten-  │
       │              │  │  authority)  │   │     box      │
       └──────┬───────┘  └──────────────┘   └──────────────┘
              │
              ▼
       ┌──────────────────────────────────────────────┐
       │             Connectors per organisation       │
       │  (Haal Centraal, sectoral APIs, mock APIs)   │
       └──┬─────┬─────┬─────┬─────┬─────┬─────┬──────┘
          ▼     ▼     ▼     ▼     ▼     ▼     ▼
       BRP  SVB   CAK   RDW   BD    KVK   ...   (12 source systems)
```

You probably will not build all of this in 36 hours. **Pick a slice you can
demo end-to-end** with the synthetic data in `data/`, and explicitly call out
in your pitch which existing building blocks the missing pieces would map to.

## What "production-grade" looks like (for the roadmap deliverable)

A team optionally addressing research question 4 (strategic roadmap) should
think about:

- **Authorisation:** Machtigen v2 with bereavement-specific profile + audit.
- **Eventing:** BRP overlijdens­signaal as a queryable event source other
  organisations subscribe to (currently push-only, partial coverage).
- **Aggregation:** Stateless aggregator that fans-out reads to source
  systems on each request, Common Ground style, with caching only for UX
  responsiveness.
- **Channels:** Bundled output via Berichtenbox + paper fallback via
  PostNL via the gemeente's existing print infrastructure.
- **Governance:** Joint controllership agreement between the 12
  organisations, anchored in BZK *Aanpak Levensgebeurtenissen*.
