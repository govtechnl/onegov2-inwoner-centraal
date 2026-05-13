# Scenarios

> **Why this file exists.** This file translates the challenge brief into 10 concrete, demo-able user stories that map directly onto the synthetic data and personas. Each scenario is small enough to prototype in a few hours, but together they cover every must-have from [`docs/beoordelingscriteria.md`](beoordelingscriteria.md).
>
> **How to use.** Pick one or two scenarios as your demo spine. Use the rest as inspiration or to stretch goals. You are *not* required to implement these - they exist to unblock teams who want a concrete starting point.

---

## 1. Unified inbox for the partner

**Persona:** Truus.
**Goal:** One screen showing every letter Truus and the erven received since Cees died, sorted chronologically with clear "actie nodig vóór …" markers.
**Data:** [`fixtures/truus-cees.json`](../data/fixtures/truus-cees.json) → `correspondentie[]`.
**Bonus:** group by organisation, show *why* the letter was sent (via [`brieven-catalogus.yaml`](../data-generation/reference/brieven-catalogus.yaml) `voorwaarden`).

## 2. "Wat moet ik nu doen?": proactive task list

**Persona:** Anneke.
**Goal:** A B1-language to-do list ranked by deadline, deduplicated across organisations.
**Data:** `verplichtingen.jsonl` + `correspondentie.jsonl` filtered on `actie_vereist == true`.
**Demo trick:** show the same list in *paper* and *digital* variants - Anneke prefers paper.

## 3. Anti-condoleance-storm

**Persona:** Truus / any partner.
**Goal:** Detect that on day 4 Truus receives 6 condoleance letters from different organisations and demo *one* combined "we leven met u mee" message instead.
**Data:** filter `correspondentie.jsonl` on `type == "condoleance"`.
**Why it matters:** mentioned explicitly in [`docs/casus-truus.md`](casus-truus.md) as a pain point.

## 4. DigiD-machtiging zonder DigiD

**Persona:** Marcus.
**Goal:** Marcus has no working DigiD. Design (and prototype) a one-time intake - paper, ID-scan, video-call, NL Wallet, anything - that grants him "machtiging namens overledene" without him having to recover DigiD first.
**Data:** [`fixtures/marcus.json`](../data/fixtures/marcus.json).
**Constraint:** must respect [`docs/juridisch-kader.md`](juridisch-kader.md) (GDPR after death + identity assurance).

## 5. Erfbelasting voorbereider

**Persona:** any.
**Goal:** Take the BRP overlijdensbericht + KVK data + Toeslagen herzieningen and pre-fill the aangifte erfbelasting (or at least show a checklist of what's needed).
**Data:** all layers for one fixture; reference rates in [`tarieven.yaml`](../data-generation/reference/tarieven.yaml).

## 6. KVK + WBSO continuity dashboard

**Persona:** Ondernemer.
**Goal:** Show erven of an eenmanszaak ondernemer the open obligations: WBSO uren-administratie, RVO subsidie eindafrekening, KVK uitschrijving deadline.
**Data:** [`fixtures/ondernemer.json`](../data/fixtures/ondernemer.json) + `kvk_rvo` block.
**Stretch:** suggest "voortzetten" vs "uitschrijven" decision support.

## 7. Letter triage with explanations

**Goal:** Upload a (real-looking) PDF letter → classify as condoleance / actie / informatie → extract deadline + summarise in plain language.
**Data:** [`brieven-catalogus.yaml`](../data-generation/reference/brieven-catalogus.yaml) gives you 30+ archetypes with deadlines and conditions to train/eval against.
**Tech hint:** even a small LLM with the catalogue as RAG context performs well.

## 8. Nabestaandenpensioen aggregator

**Persona:** Marcus / Truus.
**Goal:** Surface *all potential* pensions (state ANW, employer, private) for the partner with a single intake.
**Data:** `rechten.jsonl` filtered on `categorie ∈ {anw, nabestaandenpensioen}`.
**Why:** today the partner has to chase each pension fund individually.

## 9. Reverse-route: which organisations *should* know?

**Goal:** Given a BRP overlijdensbericht, generate the list of organisations that *should* automatically be notified (and which currently aren't).
**Data:** [`reference/organisaties.yaml`](../data-generation/reference/organisaties.yaml) → `bsn_signaal_uit_brp_bekend` flag.
**Demo:** highlight the gap between "should know" and "actually knows".

## 10. Timeline visualiser

**Goal:** Render `tijdlijn.json` as an interactive timeline (Gantt or swim-lane) so judges instantly see the *density* of touchpoints in the first 90 days.
**Data:** [`data/synthetic/tijdlijn.json`](../data/synthetic/tijdlijn.json).
**Effect:** powerful "wow" moment in a 5-minute pitch.

---

## Cross-cutting "wow" criteria

If your scenario also demonstrates **one** of the following, judges will weight it higher (see [`docs/beoordelingscriteria.md`](beoordelingscriteria.md)):

- **No DigiD assumed** - works for the locked-out partner.
- **B1-taal** - every visible string scores at B1 or below.
- **Common Ground compliant** - no data is duplicated; sources stay authoritative.
- **Cross-organisation** - at least 3 of the 12 organisations interact.
- **Reversible** - the citizen can undo what the system did on their behalf.
