# KvK inventarisatie verplichtingen (snapshot 2024-12-16)

Werkdocument van de Kamer van Koophandel met een inventarisatie van
verplichtingen, correspondentie en contactmomenten richting nabestaanden
in de eerste **3 maanden** na overlijden, in het kader van de *Aanpak
Levensgebeurtenissen — Verkenning uitstel van verplichtingen*.

## Bron

Origineel: [`../KvK - Inventarisatie verplichtingen resultaten - Niet compleet - V2024-12-16.xlsx`](../KvK%20-%20Inventarisatie%20verplichtingen%20resultaten%20-%20Niet%20compleet%20-%20V2024-12-16.xlsx)
(één werkblad, ~129 ingevulde regels, peildatum 2024-12-09).

Aangeleverd door ICTU als aanvullende achtergrond voor de OneGov #2
hackathon.

## Belangrijke caveats

> Citaat uit de begeleidende mail bij het bestand:
>
> *"Deze lijst is niet compleet, niet actueel (want uit 2024) en geldt
> vooral voor wat te doen als nabestaande van een ondernemer.
> Uiteindelijk is er wel meer informatie toegevoegd voor nabestaanden
> breder."*

Concreet betekent dat:

- **Niet compleet** — niet alle instanties of verplichtingen staan erin.
- **Niet actueel** — peildatum december 2024; wet- en beleidswijzigingen
  na die datum zijn niet verwerkt.
- **Ondernemer-bias** — vertrekpunt was *nabestaande van een ondernemer*
  (vandaar veel KVK / Belastingdienst zakelijk); particuliere onderwerpen
  zijn later toegevoegd maar minder uitgewerkt.
- **Werkdocument, geen normstelling** — gebruik het als signaal van wat
  er in de praktijk speelt, niet als juridische bron. Voor het juridisch
  kader: zie [../../docs/juridisch-kader.md](../../docs/juridisch-kader.md).

## Hoe te gebruiken in de hackathon

Geschikt als **inspiratie en checklist** voor:

- **Stap 2 — gepersonaliseerd totaaloverzicht:** welke verplichtingen,
  contactmomenten en statuswijzigingen kunnen voorkomen op één persoonlijk
  overzicht voor de nabestaande?
- **Stap 1 — gebundelde eerste brief:** welke instanties zouden
  realistisch in zo'n bundel zitten en welke acties vragen zij?
- **Knelpunten** (kolom in de inventarisatie) — waardevolle bron voor
  pijnpunten die je prototype zou kunnen wegnemen.

**Niet** geschikt als bron voor het synthetische datamodel — dat staat in
[../../data/schemas/](../../data/schemas/) en is leidend.

## Afgeleide bestanden

Voor wie niet snel even Excel wil openen:

- [inventarisatie.csv](inventarisatie.csv) — platte CSV, schone kolomnamen,
  één rij per inventarisatie-item (84 items).
- [inventarisatie.md](inventarisatie.md) — gegroepeerd per instantie,
  makkelijk te scannen of door te geven aan een LLM.
- [convert.py](convert.py) — het scriptje dat beide genereert. Alleen
  opnieuw draaien als de bron-XLSX wijzigt:

  ```powershell
  ..\..\data-generation\.venv\Scripts\python.exe convert.py
  ```

## Instanties die voorkomen

KVK, Belastingdienst (Algemeen, Inning, Inkomstenbelasting, Omzetbelasting,
Motorrijtuigenbelasting, Loonheffing, Overige middelen, Erfbelasting,
Particulieren), Toeslagen, SVB, CAK, CJIB, RDW, WAM-verzekering, BOIP /
Octrooicentrum, UWV, Gemeenten, DUO.

Vergelijk met de twaalf organisaties in de challenge-brief
([../../CHALLENGE.md](../../CHALLENGE.md)): de KvK-lijst dekt het
zakelijke domein (KVK, BOIP, loonheffing, omzetbelasting) dieper, het
particuliere domein lichter.
