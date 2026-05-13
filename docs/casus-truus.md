# Casus: Truus & Cees

> Source materials:
> [`resources/Situatie-Truus.pptx`](../resources/Situatie-Truus.pptx) and
> [`resources/Bijlage-3-correspondentie-nabestaanden.pdf`](../resources/Bijlage-3-correspondentie-nabestaanden.pdf).
>
> This file structures the original ICTU material as a per-organisation
> letter inventory you can use as ground truth when validating prototypes
> or generators.

## The situation

| Cees (deceased) | Truus (surviving partner) |
|---|---|
| 72 years old | 62 years old |
| Married to Truus | Married to Cees |
| AOW recipient (~€25k / year) | Employed (~€25k / year) |
| Lived in *verzorgingstehuis* (care home) | Lives in their rented apartment |
| Officially registered at the care home address | Receives huurtoeslag and zorgtoeslag |
| Died unexpectedly | |

This combination - a deceased partner registered at a care home, a surviving
partner at a different home address - is the hidden trap that drives most of
the addressing errors below.

## Letter inventory per organisation

The columns are:

- **When**: timing relative to the date of death.
- **Letter**: short label.
- **Salutation**: current state of the salutation.
- **Addressed to**: current state of the address.
- **Action required?**: whether Truus must act.

### RDW (Rijksdienst voor het Wegverkeer)

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| Week 1 | Information: vehicle registration transfer | "Beste erven van [Cees]" | Cees's address (care home) | Optional |
| Month 3 | Reminder: transfer ownership after death | "Beste erven van [Cees]" | Erven address (Belastingdienst-derived) | Yes |
| Month 6 | Termination of registration if not yet transferred | "Beste erven van [Cees]" | Cees's address + erven address | Yes |

> Source: `S-0068`, `S-1712`, `S-1713` documents referenced in the pptx.

### SVB (Sociale Verzekeringsbank)

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| Week 1 | ANW information letter | Personal, on partner's name | Truus's address | Informational |
| Week 1 | AOW *overlijdensuitkering* (1 month AOW + holiday pay) | Personal, on partner's name | Truus's address | None - paid automatically |
| With AOW letter | *Jaaropgave* sent on paper to last address of deceased | - | Last address of Cees | Keep - cannot be re-sent digitally |

> Note: after death, *Mijn SVB* cannot be used to view the deceased's data.
>
> Source: `1908ABN.docx`.

### CAK (Centraal Administratie Kantoor)

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| Week 1 | WLZ condolence letter | "Aan de erven van meneer …" | Cees's address (care home) | None |
| Variable | WLZ invoice | "Mevrouw Truus inzake meneer Cees" | Truus's address - *if* she registered a contact address with CAK | Yes (payment) |
| Conditional | Notice when *automatische incasso* fails (account frozen) | On name of Cees | Cees's address | Yes (resolve payment) |

### Belastingdienst: Toeslagen (zorgtoeslag, on Cees's BSN)

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| Week 1–4 | Revised decision (*herziene beschikking*) zorgtoeslag | "Aan de erven van" | Cees's address (care home) | Review |
| Within 1 week of revised decision | Recovery decision (*terugvorderingsbeschikking*) | "Aan de erven van" | Cees's address (care home) | Yes (payment) |
| ~1 year after death | Final assessment (*definitieve toekenning*) zorgtoeslag | "Aan de erven van" | Erven address (Truus) | Review |
| ~1 year after death | If outstanding amount: recovery letter OR request for bank account number | "Aan de erven van" | Erven address (Truus) | Yes |

> Pattern matches Truus's *naheffing* a year later in the persona description.

### Belastingdienst: Erfbelasting / IB

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| Week 1–5 | *Ervenbrief* | "Aan de erven van" | Cees's address (care home) | Review |
| Quarter 1 / half-year | *Aangifte erfbelasting* + many follow-ups | "Aan de erven van" | Erven address | Yes |

> Source: `ANONIEM_CONCEPT_AL780_DYN_Contactpersonen Nabestaanden`.

### Gemeente

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| Week 1 | Condolence letter | Personal | Truus's address - *if* contact details registered at *aangifte overlijden* | None |
| Variable | Parking permit transfer | - | - | Optional (and unrealistic for Cees in a care home) |
| Conditional | Local taxes (*gemeentelijke belastingen*) | - | - | Only relevant if death is in February (peildatum effect) |

> Source: NVVB sample letter `voorbeeldbrief_aan_nabestaandengemeente_parkeervergunning`.

### Waterschap (water authority)

| When | Letter | Salutation | Addressed to | Action |
|---|---|---|---|---|
| After 1 January (peildatum) | *Waterschapsbelasting* assessment | - | Address of Cees on 1 January | Yes (payment) |

> The *peildatum* is 1 January. The bill follows weeks later, by which time
> Cees may have been deceased for weeks. Truus inherits the obligation as
> heir.
>
> Source: Unie van Waterschappen statement, MAX Meldpunt coverage.

## Patterns visible across organisations

1. **Salutation chaos.** Most letters open with *"Aan de erven van …"* even
   when the recipient is the partner specifically. Only SVB and (sometimes)
   the gemeente address the partner personally.
2. **Addressing chaos.** Letters land at *Cees's last registered address*
   (the care home), at the *erven address* (which the Belastingdienst
   maintains), or at *Truus's address*, depending on the organisation, and
   on whether Truus proactively registered a contact address with that
   organisation.
3. **Timing chaos.** Some letters arrive within a week, others up to a year
   later. There is no single calendar.
4. **Action ambiguity.** Many letters are informational, but written in a
   tone that suggests they require action. Conversely, the
   *terug­vorderings­beschikking* a year later genuinely requires action and
   is easy to miss.
5. **Peildatum effects.** The water authority and Belastingdienst use a
   reference date (often 1 January). Death between the reference date and
   the assessment date does not relieve the obligation, Truus inherits it.

## Use as ground truth

When generating Truus's correspondence stream synthetically, the rows above
should appear in [`data/fixtures/truus-cees.json`](../data/fixtures/truus-cees.json)
as a hand-curated golden record. Any prototype claiming to "give Truus an
overview" should at minimum surface every row in this table.
