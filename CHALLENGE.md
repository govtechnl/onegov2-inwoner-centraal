# Challenge Brief | Inwoner Centraal: Nabestaanden

> **OneGov #2** · ICTU · 4–5 June 2026 · The Hague Tech
>
> *From chaos to control: one government overview for bereaved partners.*
>
> **Challenge owners:** Natalie Moreno Robles & Ingrid Verhage (ICTU)
> **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)

This is an English working translation of the original Dutch challenge brief.
The authoritative source is the challenge brief on Junction.

---

## Background

Losing a partner triggers one of the hardest periods in a person's life. On
top of grief comes an administrative storm: bereaved partners receive
correspondence from up to **twelve government organisations** - Gemeente, SVB,
CAK, RDW, Waterschap, Belastingdienst, Toeslagen, RVO, CJIB, UWV, DUO, KVK -
each operating from its own silo, without coordination. The same details are
requested over and over while the bereaved partner's *doenvermogen* (capacity
to act under emotional pressure) is at its lowest.

The *Programma Mens Centraal* and the *Aanpak Levensgebeurtenissen* (BZK) have
extensively researched the problem. The pain points are clear. **What is
missing is a working prototype** that shows how the government could approach
this differently - proactively, personally, and from a single coherent view.
That is the space ICTU offers your team during OneGov #2.

## Problem statement

Bereaved partners face an impossible combination: grieving while having to act.
The government unintentionally amplifies that tension because:

- There is no overview of what is outstanding, not even within a single
  organisation.
- Bereaved partners must repeatedly supply the same data - contact person,
  bank account, relationship to the deceased - to every desk separately.
- The deceased's DigiD is revoked immediately upon death, blocking digital
  access to relevant records.
- There is no predictability: bereaved partners do not know which letters
  will arrive, when, or what will be expected of them.

Information overload combined with low *doenvermogen* leads to back-payments
and fines - harmful to the bereaved and costly for government organisations.

## The challenge

> *How can we help bereaved partners get a complete picture of their rights
> and outstanding obligations with the government quickly and without extra
> burden, through a proactive, personalised approach in which the government
> pre-arranges as much as possible itself?*

## Two steps toward the ideal situation

ICTU has framed the ambition in two concrete steps. Teams pick one as their
focus, or show how both connect.

### Step 1: The bundled first letter

A single letter on behalf of the whole government, sent shortly after the
death. Personal, empathic, with a clear overview of what is coming.

Includes:

- Personal salutation, no *"Aan de erven van"*.
- Things automatically arranged where possible (e.g. stopping toeslagen).
- Overview of what is still coming and when.
- Option to defer obligations.

### Step 2: The personalised total overview

A digital loket where the bereaved sees all running obligations and rights at
a glance, based on data from multiple organisations.

Includes:

- Centralised data from multiple uitvoeringsorganisaties.
- Insight into the basis on which decisions are made.
- One loket for questions and access to data.
- The ability for the bereaved to correct or request deferral.

## Guiding research questions

ICTU framed four questions teams can use as a compass:

1. **Can we retrieve data** about obligations and rights from multiple
   government organisations? Are there existing building blocks or
   infrastructure that make this possible?
2. **Can we process that data** into a personalised message that fits the
   individual situation of the bereaved partner?
3. **Can we expose this data through a single loket** so that civil servants
   *and* the bereaved themselves can see all running obligations on the BSN
   of the deceased?
4. **Can we sketch a strategic roadmap** from the current to the ideal
   situation, taking service design, technology, processes, and law &
   regulation into account?

**Optional extension:** if the deceased ran their own business, KVK, VAT
returns, and WBSO obligations also come into play. Data is optionally
available, see the data chapter.

## Personas: who you are helping

You build for one government, but you design for people. The four personas
below reflect the diversity of situations and needs, based on extensive user
research by ICTU. The Truus & Cees case (see [docs/casus-truus.md](docs/casus-truus.md))
shows per organisation which letters arrive when.

### 01 · Truus, 62

Truus is married to Cees (72), who lived in a care home and died unexpectedly.
She works, has an income of €25,000 per year, and receives huurtoeslag and
zorgtoeslag. After his death she receives letters from Gemeente, SVB, CAK,
RDW, Waterschap, Belastingdienst, Toeslagen - each addressed to *"de erven
van"*, sent to the address of the care home.

Hits these problems:

- Letters arrive at the wrong address.
- Salutation is impersonal.
- She does not know whether she must act or whether things are handled
  automatically.
- A year later she gets a back-payment claim for huurtoeslag she had not
  seen coming.

> "I never thought I would feel guilty about a letter I had overlooked."

### 02 · Marcus, 48

Marcus lost his partner suddenly to a heart attack. They had no joint
mortgage and no children, but a registered partnership. Marcus is digitally
skilled and tries to stay in control, but hits a wall: he cannot reach his
partner's digital records because the DigiD has been closed.

Hits these problems:

- Cannot log in to MijnOverheid or Toeslagen for the deceased's data.
- Receives contradictory information from two agencies.
- Wants one central loket but only finds separate phone numbers.

> "I called three times and got three different answers. How am I supposed to
> know what is correct?"

### 03 · Anneke, 71

Anneke lost her husband (74). She is less digitally skilled, dependent on
postal mail, and overwhelmed by letters in legal language. Her daughter helps,
but lives far away. Anneke does not know which letters are urgent and which
she can ignore.

Hits these problems:

- Cannot tell information letters from action letters.
- Experiences the tone as cold and distant.
- In a panic throws away a letter she later turns out to need.

> "I did not understand what to do. And there was no one to explain it to me."

### 04 · The bereaved entrepreneur (variable, optional extension)

The deceased had a sole proprietorship or was a freelancer. On top of the
private administration come business obligations: KVK deregistration, VAT
return, WBSO obligations, outstanding invoices.

Hits these problems:

- Private and business administration intertwine.
- KVK sends multiple letters to the registered address.
- The bereaved does not know which business obligations transfer and which
  expire.

> "I did not even know he still had an active subsidy at RVO. I only heard
> about it six months later."

## Data

ICTU is working with Logius to make synthetic data available for this
challenge. The data contains no personal data of real citizens and is designed
so teams can start immediately.

### Data layers (synthetic: available via this repo)

1. **Death registration & relationships (BRP-style).** BSN of the deceased
   and partner, type of relationship (married, registered partnership,
   cohabiting), date and municipality of death, residential address. The core
   layer from which everything else follows.
2. **Outstanding obligations of the deceased.** Toeslagen (zorg, huur),
   income-tax assessments, inheritance tax (terms and amounts), outstanding
   WMO provisions (e.g. mobility scooter), pension and AOW status.
3. **Rights of the surviving partner.** ANW benefit (SVB), survivor pension,
   any toeslag recalculation, right to social assistance or income support
   on income drop.
4. **Correspondence stream: simulated letter flow per organisation.** Based
   on the inventory of *Aanpak Levensgebeurtenissen* (BZK, 2025): a simulated
   sequence from the 12 organisations. Per letter: sender, type
   (information / action / invoice / reminder), timing after death, action
   required yes/no, and addressing. This is the heart of the chaos that
   bereaved partners experience today, and the basis for the overview you
   build.
5. **Timeline of expected government actions.** Per organisation: when does
   it normally send a message, which action follows when, and what is the
   legal term? This makes "predictability" a possible feature of your
   prototype.
6. **(Optional) Business data of the deceased: KVK registration.** KVK number,
   VAT status, WBSO obligations, running RVO subsidies. Availability is to
   be confirmed.

> ℹ️ Datasets are published in this repository at the latest **two weeks
> before the hackathon**, and via the Junction platform. Natalie and Ingrid
> are available on the day for substantive questions about the data and
> domain.

## Judging criteria

Teams are judged by an expert jury with domain expertise in digital
government services, AI, and technology. Four levels:

### ✅ Must: minimum requirements for a valid submission

- The solution is demonstrably useful to the bereaved partner - not only to
  the government internally.
- The prototype demonstrably works with the supplied data (or a self-composed
  variant).
- A linkage is made between **at least two** government organisations in the
  overview.

### ⭐ Should: distinguishing qualities

- The solution is proactive: the government initiates, the bereaved does not
  have to search.
- Attention to tone, timing, and intelligibility - not only completeness.
- The solution accounts for people with low digital *doenvermogen* or
  limited language proficiency.

### ⚠️ Should not: pitfalls to avoid

- A solution that fixes the problem only internally (for civil servants),
  without effect on the bereaved.
- Building as if you could change every existing system and process. Reason
  from existing building blocks.

### ✨ Could: bonus for outstanding submissions

- An open-source approach with reusable components.
- Comparison with or alignment to existing tools (rijksoverheid.nl/overlijden,
  Berichtenbox, MijnOverheid).
- A modular design that scales to other life events (divorce, disability,
  retirement).

## Deliverables

At the end of the hackathon every team presents:

- A **working prototype or demo**, even if not finished, show the core.
- A short **pitch** (max. 5 minutes + Q&A) for the expert jury.
- A **pitch deck** (max. 10 slides).
- A **repository link** if you wrote code (GitHub, GitLab, or similar).
- A short description: what you built, for whom, and why.

## Legal framework: what you should know

When designing a solution for bereaved partners you encounter several legal
frameworks. You do not need to be a lawyer, but it helps to know them.

- **GDPR after death.** In the Netherlands the GDPR does not apply to data of
  deceased persons. This creates more room for data sharing between
  organisations, but the Wet BRP, Wet SUWI, and sectoral legislation do set
  limits on access and use.
- **DigiD authorisation.** The DigiD of the deceased lapses on death. The
  Belastingdienst offers a *nabestaandenmachtiging* at the desk; Logius is
  working on broader solutions. In your prototype you may assume this
  authorisation is available.
- **BRP as starting point.** A death is registered in the Basisregistratie
  Personen (BRP). However, this signal does not automatically reach all
  government organisations. In the prototype you may assume that linkage on
  this signal is legally possible (or will be).
- **Existing standards.** Alignment with the NL API Strategy, the
  Berichtenbox (Logius), and Common Ground architecture is appreciated by
  the jury.

See [docs/juridisch-kader.md](docs/juridisch-kader.md) for more detail.

## Resources and inspiration

- [rijksoverheid.nl/overlijden](https://www.rijksoverheid.nl/overlijden): central overview for bereaved partners.
- [digitaleoverheid.nl/aanpaklevensgebeurtenissen](https://www.digitaleoverheid.nl/aanpaklevensgebeurtenissen): *Aanpak Levensgebeurtenissen* (BZK), incl. inventory of letter flows from 12 organisations.
- [programmamenscentraal.nl](https://www.programmamenscentraal.nl): *Programma Mens Centraal* research reports 2018–2024.
- [belastingdienst.nl](https://www.belastingdienst.nl): *Nabestaandenmachtiging*.
- [developer.overheid.nl](https://developer.overheid.nl): NL API Strategy.
- [commonground.nl](https://commonground.nl): Common Ground architecture principles.
- [resources/](resources/): original source material in this repo (DOCX, PPTX, PDF).

## Disclaimer

The supplied data is fully synthetic and contains no personal data of real
citizens. The challenge is intended as an innovation exercise. Prototypes
that emerge from the hackathon are not policy commitments and require further
review before they can go into production.

---

**Challenge owners:**
Natalie Moreno Robles · `Natalie.MorenoRobles@ictu.nl`
Ingrid Verhage · `Ingrid.Verhage@ictu.nl`

**Hackathon questions:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)
