
# Implementation Plan: Fantasy Football Intelligent Advisor App

**Branch**: `001-fantasy-football-intelligent` | **Date**: 2025-09-26 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `G:\specify\faintasy\specs\001-fantasy-football-intelligent\spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from file system structure or context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
AI-powered fantasy football assistant manager that analyzes ESPN league data, monitors NFL news, and provides automated recommendations for lineup decisions, trades, and waiver wire pickups. Designed for novice players who want competitive guidance without deep fantasy football knowledge. Features real-time notifications, educational explanations, and adaptive learning from user decisions.

## Technical Context
**Language/Version**: Python 3.11+ (existing espn_api codebase is Python 3, targeting modern versions)  
**Primary Dependencies**: espn_api (existing ESPN integration), FastAPI (web API), Click (CLI), requests (HTTP client), Playwright/Puppeteer (web scraping fallback), Ollama (local AI), PostgreSQL (persistent storage), Qdrant (vector embeddings)  
**Storage**: PostgreSQL for relational data (users, leagues, teams, recommendations), Qdrant vector database for AI similarity search and embeddings  
**Testing**: pytest (unit tests), pytest-asyncio (async testing), requests-mock (API mocking), testcontainers (integration testing)  
**Target Platform**: Linux/Windows servers, containerized deployment with Docker  
**Project Type**: single (extended library with CLI interface, following constitution)  
**Performance Goals**: < 5 minutes for recommendations, < 2 minutes for notifications, 99% API uptime during NFL season  
**Constraints**: Real-time ESPN data sync required, privacy-focused (no external AI services), offline-capable for core features, < 500MB memory usage per user  
**Scale/Scope**: 100+ concurrent users, 10-50 leagues per user, 15-week NFL season + playoffs, historical data retention

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

✅ **I. Library-First**: Fantasy football advisor will be implemented as standalone libraries (`ff_advisor.core`, `ff_advisor.ai`, `ff_advisor.espn`) that are self-contained, independently testable, and documented. Each library has clear purpose (core=recommendations, ai=analysis, espn=data).

✅ **II. CLI Interface**: All functionality exposed via CLI commands using Click framework (`ff-advisor analyze`, `ff-advisor recommend`, `ff-advisor sync`). Text-based input/output with both JSON and human-readable formats supported.

✅ **III. Test-First (NON-NEGOTIABLE)**: TDD mandatory for all components. Tests written and failing before implementation. Contract tests for ESPN API integration, unit tests for recommendation algorithms, integration tests for full workflows.

✅ **IV. Integration Testing**: Critical integration points covered: ESPN API authentication, database persistence, AI model inference, notification delivery, web scraping fallbacks.

✅ **V. Observability & Versioning**: Structured logging throughout system (JSON format), semantic versioning for all public APIs, text I/O ensures debuggability, performance metrics tracked.

## Project Structure

### Documentation (this feature)
```
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
# Fantasy Football Advisor - Extended espn_api library
espn_api/                    # Existing ESPN API library
├── football/                # Existing football module
└── [existing modules...]

ff_advisor/                  # New: Fantasy Football Advisor module
├── __init__.py
├── core/                    # Core recommendation logic
│   ├── __init__.py
│   ├── analyzer.py          # Fantasy analysis engine
│   ├── recommender.py       # Recommendation generator
│   └── decision_tracker.py  # Learning from user decisions
├── ai/                      # AI/ML components
│   ├── __init__.py
│   ├── embeddings.py        # Ollama integration for text embeddings
│   ├── similarity.py        # Player/matchup similarity analysis
│   └── news_analyzer.py     # NFL news sentiment analysis
├── data/                    # Data persistence layer
│   ├── __init__.py
│   ├── models.py            # SQLAlchemy models
│   ├── repositories.py      # Data access patterns
│   └── vector_store.py      # Qdrant vector database client
├── integrations/            # External integrations
│   ├── __init__.py
│   ├── espn_client.py       # Enhanced ESPN API wrapper
│   ├── news_scrapers.py     # NFL news aggregation
│   └── notifications.py     # Push notification service
├── web/                     # FastAPI web interface (optional)
│   ├── __init__.py
│   ├── api.py               # REST API endpoints
│   └── models.py            # Pydantic models
└── cli/                     # CLI interface (constitutional requirement)
    ├── __init__.py
    ├── commands/            # Click command groups
    │   ├── analyze.py       # Analysis commands
    │   ├── recommend.py     # Recommendation commands
    │   └── sync.py          # Data sync commands
    └── formatters.py        # Output formatting (JSON/human-readable)

tests/                       # Extended test suite
├── ff_advisor/              # New tests for advisor
│   ├── unit/                # Unit tests
│   │   ├── test_analyzer.py
│   │   ├── test_recommender.py
│   │   └── test_ai/
│   ├── integration/         # Integration tests
│   │   ├── test_espn_integration.py
│   │   ├── test_database.py
│   │   └── test_ai_pipeline.py
│   └── contract/            # Contract tests
│       ├── test_espn_api.py
│       └── test_cli_interface.py
└── [existing espn_api tests...]

migrations/                  # Database migrations
├── versions/
└── alembic.ini

config/                      # Configuration files
├── database.yml
├── logging.yml
└── app_settings.yml
```

**Structure Decision**: Single project extension to existing espn_api library. Following constitutional Library-First principle, the fantasy advisor is implemented as separate libraries (core, ai, data, integrations) that extend the existing ESPN API foundation. CLI interface mandatory per constitution, optional web API for future expansion.

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:
   ```
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests** from contracts:
   - One test file per endpoint
   - Assert request/response schemas
   - Tests must fail (no implementation yet)

4. **Extract test scenarios** from user stories:
   - Each story → integration test scenario
   - Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType copilot`
     **IMPORTANT**: Execute it exactly as specified above. Do not add or remove any arguments.
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base template structure
- Analyze Phase 1 artifacts to extract implementation requirements:
  - Parse `data-model.md` for 9 core entities → database model creation tasks
  - Parse `contracts/cli_interface.md` for command specifications → CLI implementation tasks
  - Parse `contracts/espn_api.md` for integration requirements → adapter implementation tasks
  - Extract functional requirements FR-001 through FR-018 from spec.md → feature implementation tasks

**Task Categorization & Prioritization**:
1. **Foundation Tasks [P]** (Parallel execution possible):
   - Database schema setup and migrations
   - Core entity models (User, League, Team, Player, Matchup, Recommendation, NewsItem, Transaction, AnalysisEngine)
   - Repository interfaces and implementations
   
2. **Contract Test Tasks [P]** (Constitutional TDD requirement):
   - ESPN API integration contract tests
   - CLI interface contract tests  
   - Database repository contract tests
   - External news source contract tests

3. **Service Layer Tasks** (Sequential dependencies):
   - ESPN data synchronization service
   - Recommendation engine core algorithms
   - News aggregation and analysis pipeline
   - Notification delivery system

4. **Integration Tasks**:
   - AI/ML model integration (Ollama embeddings)
   - Vector database operations (Qdrant)
   - Background task processing (Celery)
   - Full user workflow integration tests

5. **CLI Interface Tasks** (Constitutional requirement):
   - Command group implementations (`analyze`, `recommend`, `sync`)
   - Output formatters (JSON and human-readable)
   - Error handling and user feedback

**Ordering Strategy**:
- **Constitutional TDD**: All contract tests must be written and failing before implementation
- **Dependency Flow**: Models → Repositories → Services → Integration → CLI
- **Parallel Opportunities**: Independent models, contract tests, and utility functions marked [P]
- **Critical Path**: ESPN integration and recommendation engine are primary dependencies

**Task Template Structure**:
Each task will include:
- Clear acceptance criteria from functional requirements
- Test scenarios derived from user acceptance scenarios  
- Dependencies on other tasks or external systems
- Estimated complexity and time requirements
- Constitutional compliance checkpoints (Library-First, CLI Interface, Test-First)

**Quality Gates**:
- Phase 0 gate: All contract tests passing (interfaces defined)
- Phase 1 gate: Core models and repositories complete
- Phase 2 gate: Services integrated and recommendation engine functional
- Final gate: Full user workflows working end-to-end via CLI

**Estimated Output**: 25-30 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |


## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command) - ✅ research.md generated with technology stack and architecture decisions
- [x] Phase 1: Design complete (/plan command) - ✅ data-model.md, contracts/, quickstart.md all generated
- [x] Phase 2: Task planning complete (/plan command - describe approach only) - ✅ Comprehensive task generation strategy defined
- [ ] Phase 3: Tasks generated (/tasks command) - Ready for execution
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS - All 5 constitutional principles verified (Library-First, CLI Interface, Test-First, Integration Testing, Observability)
- [x] Post-Design Constitution Check: PASS - Phase 1 artifacts maintain constitutional compliance
- [x] All NEEDS CLARIFICATION resolved - Feature specification contains comprehensive clarifications from Session 2025-09-26
- [x] Complexity deviations documented - No constitutional violations identified

**Artifacts Generated**:
- [x] `plan.md` - This implementation plan with technical context and structure
- [x] `research.md` - Technology stack decisions and architecture patterns  
- [x] `data-model.md` - 9 core entities with relationships and vector embeddings
- [x] `contracts/cli_interface.md` - Complete CLI command specifications
- [x] `contracts/espn_api.md` - ESPN integration contract definitions
- [x] `quickstart.md` - User onboarding guide with novice-friendly explanations

**Ready for /tasks Command**: ✅ All Phase 0-2 requirements complete, comprehensive artifacts available for task generation

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*
