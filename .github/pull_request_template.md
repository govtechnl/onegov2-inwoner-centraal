<!--
Thanks for contributing to OneGov #2 | Inwoner Centraal: Nabestaanden.

Hackathon teams: this repository is the central library. Your team's
prototype lives in your own repository and is submitted via Alkemio.
PRs against this repo are welcome for reusable artefacts (schemas,
fixtures, generator improvements, documentation, persona refinements).
-->

## Summary

<!-- One or two sentences. What does this change and why? -->

## Type of change

- [ ] Documentation (CHALLENGE.md, README.md, docs/)
- [ ] Schema (data/schemas/)
- [ ] Fixture (data/fixtures/)
- [ ] Generator (data-generation/)
- [ ] CI / tooling
- [ ] Other:

## Track and actions covered (hackathon teams only)

Which track does the linked prototype focus on?

- [ ] Stap 1: De gebundelde eerste brief
- [ ] Stap 2: Het gepersonaliseerde totaaloverzicht
- [ ] Hybrid / both

Which of the three actions from the brief does the prototype cover?

- [ ] Informeren (telling the bereaved partner what is coming, in plain language)
- [ ] Toegang geven (delegated access to the deceased's records, single loket)
- [ ] Handelen namens (the government pre-arranges what it can)

Linked Alkemio submission: <!-- paste your team's Alkemio entry URL -->
Linked prototype repository: <!-- paste your team's GitHub / GitLab URL -->

## Checklist

- [ ] No real personal data; every record carries `"synthetic": true` and `"bron": "onegov2-inwoner-centraal-generator"`.
- [ ] Schemas, generator, and fixtures stay in sync.
- [ ] `pytest -v` and `ruff check .` pass locally in `data-generation/`.
- [ ] Internal links in changed Markdown files resolve.
- [ ] Licensing is compatible with this repo: code under Apache-2.0, data and docs under CC BY 4.0 (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Related issues / context

<!-- Fixes #..., Refs #..., or links to challenge brief sections. -->
