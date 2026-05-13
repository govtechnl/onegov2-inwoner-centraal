# Legal framework: what you should know

> *You do not need to be a lawyer to compete. But knowing where the legal
> walls and doors are will save you from designing a prototype that cannot
> exist in reality.*

This document summarises the legal context referenced in
[`CHALLENGE.md`](../CHALLENGE.md). For authoritative interpretation, consult
the original sources or the *Rijksoverheid* legal teams. None of the below
is legal advice.

## 1. GDPR after death

The General Data Protection Regulation (GDPR / *AVG*) applies only to *living*
natural persons. In the Netherlands the GDPR does **not** apply to data of
deceased persons (Recital 27).

**Implications for the challenge:**

- There is more legal room to share data *about the deceased* between
  organisations than during life.
- This does **not** mean a free-for-all. Sectoral legislation continues to
  apply:
  - **Wet BRP** governs access to civic registry data.
  - **Wet SUWI** governs data exchange in social security.
  - The Belastingdienst, CAK, RDW, etc. each have their own statutory
    bases for processing.
- Data about the **surviving partner** *is* personal data and remains fully
  subject to the GDPR.

**Design heuristic.** Keep deceased-data and partner-data clearly separated
in your model. Sharing the former across organisations is far easier than
sharing the latter.

## 2. DigiD lapses on death

The DigiD of the deceased is revoked immediately upon registration of death
in the BRP. This is the source of Marcus's pain in
[`personas.md`](personas.md#02--marcus-48--the-locked-out-partner).

**Current workarounds.**

- The Belastingdienst offers a *nabestaanden­machtiging* at the desk -
  a paper-based delegated authorisation.
- Logius is working on broader, programmatic solutions.

**For the prototype.** The challenge brief explicitly states you may assume
the *nabestaanden­machtiging* is available digitally. Model it as a scoped,
time-limited, audit-logged delegation - not as a copy of the deceased's
DigiD.

## 3. BRP as the trigger event

A death is registered by the gemeente in the **Basisregistratie Personen
(BRP)**. From there, the signal in principle propagates to:

- SVB (AOW, ANW)
- Belastingdienst
- CAK
- UWV
- Pension funds (via APG / pension administrators)
- Gemeente (own systems)

The signal does **not** automatically reach RDW, Waterschap, KVK, Toeslagen
back-office systems, CJIB, RVO, DUO, banks, insurers, energy companies, or
private parties. Each organisation has its own update cadence.

**For the prototype.** The brief permits you to assume that linkage on the
BRP overlijdens­signaal is, or will be, legally and technically possible
across the 12 organisations in scope. This is a deliberate simplification
to keep the focus on service design, not infrastructure debate.

## 4. Existing standards to align with

Alignment with these standards is rewarded by the jury (see
[`beoordelingscriteria.md`](beoordelingscriteria.md), the "✨ Could" tier).

| Standard | What it gives you |
|---|---|
| **NL API Strategie** ([developer.overheid.nl](https://developer.overheid.nl)) | Conventions for REST APIs across NL government, including pagination, versioning, error responses, and OAS profiles. |
| **Common Ground** ([commonground.nl](https://commonground.nl)) | Architecture principles separating data, services, and applications. Encourages re-use of authentic registries instead of copies. |
| **Berichtenbox / MijnOverheid** | The existing channel for digital government correspondence to citizens. A bundled letter likely flows through here. |
| **Logius infrastructure** | DigiD, Digipoort, Stelselcatalogus, Haal Centraal - the plumbing your prototype can lean on. |
| **NORA** ([noraonline.nl](https://www.noraonline.nl)) | Reference architecture for the Dutch government, including service principles. |

## 5. Specific data-sharing instruments worth knowing

- **Haal Centraal BRP API**: modern read-API on top of BRP data. Already
  used by RDW, Belastingdienst, gemeenten.
- **Stelsel van Basisregistraties**: the 10 official base registries
  (BRP, BAG, BRK, NHR, BRV, BRT, BGT, BRO, BRI, RGT). Trust these for
  authoritative facts.
- **Eenduidige Normatieve Onderdelen (ENO)**: work in progress on
  standardised concepts across registries.
- **NL Wallet** ([edi.pleio.nl](https://edi.pleio.nl)): the upcoming Dutch
  EUDI Wallet may eventually carry the *nabestaanden­machtiging*.

## 6. Things you should *not* assume

- That you can change source-system schemas of UWV, SVB, Belastingdienst,
  etc. Reason from existing APIs and from data you can pull, not push.
- That the Berichtenbox is opt-out by default. It is opt-in.
- That you can collect new personal data of the surviving partner without a
  legal basis. If your design needs e.g. a phone number, justify it.
- That all 12 organisations will agree on a unified salutation policy
  tomorrow. The bundling can happen at a higher layer.

## 7. Reading list

- [Aanpak Levensgebeurtenissen - BZK](https://www.digitaleoverheid.nl/aanpaklevensgebeurtenissen)
- [Programma Mens Centraal](https://www.programmamenscentraal.nl) - research reports 2018–2024
- [Rijksoverheid - Overlijden](https://www.rijksoverheid.nl/overlijden)
- [Belastingdienst - Nabestaandenmachtiging](https://www.belastingdienst.nl/wps/wcm/connect/nl/contact/content/dat-doe-ik-voor-iemand-anders)
- [Wet Basisregistratie Personen](https://wetten.overheid.nl/BWBR0033715)
- [GDPR Recital 27 - does not apply to deceased persons](https://gdpr-info.eu/recitals/no-27/)
