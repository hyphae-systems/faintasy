
<!--
Sync Impact Report
Version change: (none) → 1.0.0
Modified principles: [all placeholders filled]
Added sections: Technology & Compliance, Development Workflow
Removed sections: None
Templates requiring updates: ✅ plan-template.md, ✅ spec-template.md, ✅ tasks-template.md
Follow-up TODOs: TODO(RATIFICATION_DATE): Original adoption date required from project owner
-->

# espn-api Constitution


## Core Principles

### I. Library-First
Every feature starts as a standalone library. Libraries MUST be self-contained, independently testable, and documented. Each library MUST have a clear purpose—organizational-only libraries are not permitted.

### II. CLI Interface
Every library MUST expose its functionality via a CLI. All commands MUST use text in/out protocols: stdin/args for input, stdout for output, and errors to stderr. Both JSON and human-readable formats MUST be supported.

### III. Test-First (NON-NEGOTIABLE)
Test-Driven Development (TDD) is mandatory: Tests MUST be written and approved before implementation. Tests MUST fail before code is written. The Red-Green-Refactor cycle is strictly enforced.

### IV. Integration Testing
Integration tests are REQUIRED for new library contracts, contract changes, inter-service communication, and shared schemas. All integration points MUST be covered by tests.

### V. Observability & Versioning
Text I/O ensures debuggability. Structured logging is REQUIRED. Semantic versioning (MAJOR.MINOR.PATCH) MUST be used for all public interfaces. Breaking changes MUST increment the MAJOR version.


## Technology & Compliance

All code MUST target Python 3.8 or higher. Code style MUST follow PEP8. Dependencies MUST be managed via requirements.txt and/or pyproject.toml. Security best practices and compliance with open-source licenses are REQUIRED.


## Development Workflow

All code changes MUST be submitted via Pull Request and reviewed by at least one maintainer. TDD is enforced: All tests MUST pass before merging. Releases MUST be tagged and changelogs updated. Issue reporting and discussions are encouraged via GitHub Issues and Discussions.


## Governance

This constitution supersedes all other project practices. Amendments require documentation, approval by project maintainers, and a migration plan if breaking. All PRs and reviews MUST verify compliance with these principles. Versioning of the constitution follows semantic versioning: MAJOR for principle removals or redefinitions, MINOR for new principles or expanded guidance, PATCH for clarifications or non-semantic refinements. Compliance reviews are expected at least quarterly.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date required from project owner | **Last Amended**: 2025-09-26
<!-- Version: 1.0.0 | Ratified: TODO(RATIFICATION_DATE): Original adoption date required from project owner | Last Amended: 2025-09-26 -->