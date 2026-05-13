# Glossary

Quick reference for acronyms and terms used throughout this repository. Aimed at international participants and non-domain reviewers.

## People & registration

| Term | Full name | What it is |
|---|---|---|
| **BSN** | Burgerservicenummer | Dutch citizen service number (9 digits, 11-proof). Primary identifier for natural persons. |
| **BRP** | Basisregistratie Personen | The municipal personal records database. Source of truth for births, deaths, marriages, addresses. |
| **RNI** | Registratie Niet-Ingezetenen | Sub-register of the BRP for non-residents. |
| **GBA** | Gemeentelijke Basisadministratie | Pre-2014 name of the BRP. Still appears in older docs. |

## Income, pensions, benefits

| Term | Full name | What it is |
|---|---|---|
| **AOW** | Algemene Ouderdomswet | State pension. Eligibility starts at the AOW-leeftijd (currently ~67). |
| **ANW** | Algemene nabestaandenwet | Surviving-dependants benefit for partners under AOW age. Means-tested. |
| **WLZ** | Wet langdurige zorg | Long-term care act. Funds nursing homes and intensive care. CAK collects the eigen bijdrage. |
| **WMO** | Wet maatschappelijke ondersteuning | Municipal social support (home care, mobility aids). |
| **WW / WIA** | Werkloosheidswet / Wet werk en inkomen naar arbeidsvermogen | Unemployment / disability benefits. UWV. |
| **IB** | Inkomstenbelasting | Income tax. The "F-biljet" is the tax return for the year of death. |
| **BOR** | Bedrijfsopvolgingsregeling | Tax relief when inheriting a business. |

## Organisations

| Acronym | Organisation | Role in deceased journey |
|---|---|---|
| **SVB** | Sociale Verzekeringsbank | Pays AOW, ANW, kinderbijslag. |
| **CAK** | Centraal Administratie Kantoor | Bills WLZ eigen bijdrage. |
| **CJIB** | Centraal Justitieel Incassobureau | Collects fines (verkeersboetes). |
| **DUO** | Dienst Uitvoering Onderwijs | Student loans / grants. |
| **RDW** | Rijksdienst voor het Wegverkeer | Vehicle registration. |
| **RVO** | Rijksdienst voor Ondernemend Nederland | Business subsidies (SDE++, EIA, MIA/Vamil). |
| **KVK** | Kamer van Koophandel | Chamber of Commerce. Handelsregister + business deregistration. |
| **UWV** | Uitvoeringsinstituut Werknemersverzekeringen | Employee insurance (WW, WIA, pensioen). |
| **ICTU** | Stichting ICTU | Public ICT advisory foundation. Organiser of this challenge. |
| **Logius** | - | Operates DigiD, MijnOverheid, Berichtenbox, Notify NL. |

## Government platforms & APIs

| Term | What it is |
|---|---|
| **DigiD** | National authentication for citizens. Required for most digital government services. |
| **DigiD Machtigen** | Authorisation: act on behalf of someone else (e.g. a deceased relative). |
| **MijnOverheid** | Citizen portal aggregating personal data and "Lopende Zaken". |
| **Berichtenbox** | Secure inbox where government bodies place official letters digitally. |
| **eHerkenning** | Authentication for businesses (the B2B equivalent of DigiD). |
| **Notify NL** | Transactional notification service (email/SMS/letter). |
| **Haal Centraal** | API standard for retrieving authentic registry data (BRP, BAG, KVK). |
| **Stelselcatalogus** | Catalogue of authentic data definitions across government. |
| **Common Ground** | Architecture vision: separate data (sources) from process (apps). |
| **NORA** | Nederlandse Overheid Referentie Architectuur. |
| **NL API Strategie** | National guidelines for designing government APIs. |
| **NL Wallet** | EU-aligned digital identity wallet (in development). |

## Common Ground APIs

| Acronym | Full name | Purpose |
|---|---|---|
| **ZGW** | Zaakgericht Werken APIs | Standard Cases / Documents / Catalogue APIs. |
| **OpenZaak** | - | Open-source ZGW implementation. |
| **Klantinteracties API** | - | Standard for recording citizen contacts. |

## Toeslagen (allowances)

| Term | What it is |
|---|---|
| **Zorgtoeslag** | Health-insurance allowance. |
| **Huurtoeslag** | Rent allowance. |
| **Kinderopvangtoeslag** | Childcare allowance. |
| **Definitieve toekenning** | Final assessment after the tax year - typically results in a refund or claw-back. |

## Business / R&D incentives

| Acronym | Full name | Purpose |
|---|---|---|
| **WBSO** | Wet Bevordering Speur- en Ontwikkelingswerk | R&D wage-tax credit. Requires hour administration. |
| **SDE++** | Stimulering Duurzame Energieproductie | Sustainable-energy subsidy. |
| **EIA** | Energie-investeringsaftrek | Energy-investment tax deduction. |
| **MIA / Vamil** | Milieu-investeringsaftrek / Willekeurige afschrijving milieu-investeringen | Environmental-investment tax incentives. |
| **KOR** | Kleineondernemersregeling | VAT exemption for small businesses. |

## Legal / privacy

| Term | What it is |
|---|---|
| **AVG / GDPR** | Algemene Verordening Gegevensbescherming. Note: GDPR does **not** apply to deceased persons in NL - but family members' data does. |
| **WGS** | Wet gegevensverwerking door samenwerkingsverbanden | Limits on data sharing across organisations. |
| **Erven** | Heirs. Until they accept/reject the estate, they are "potentiële erven". |
| **Nalatenschap** | The estate. Can be aanvaard, beneficiair aanvaard, or verworpen. |

## Document & event types in this repo

| Term | What it is |
|---|---|
| **Overledene** | Deceased person record (layer 1). |
| **Verplichting** | Outstanding obligation of the deceased toward an organisation (layer 2). |
| **Recht** | Right or potential entitlement of the surviving partner (layer 3). |
| **Correspondentie** | Letter or message sent by an organisation (layer 4). |
| **Tijdlijn** | Reference timeline of expected events per organisation (layer 5). |
| **KVK / RVO** | Business-side data (layer 6, optional). |
| **Aanhef** | Salutation line of a letter ("Geachte mevrouw…"). |
| **Geadresseerde** | Addressee category: overledene / erven / partner / contactpersoon. |
| **Peildatum** | Reference date used to determine entitlement (e.g. 1 January for waterschapsbelasting). |
