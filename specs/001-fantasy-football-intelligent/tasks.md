# Tasks: Fantasy Football Intelligent Advisor App

**Input**: Design documents from `G:\specify\faintasy\specs\001-fantasy-football-intelligent\`
**Prerequisites**: plan.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅

## Execution Flow (/tasks command output)
```
1. Loaded plan.md → Python 3.11+, FastAPI, PostgreSQL, Qdrant, Ollama, Click CLI
2. Loaded data-model.md → 9 entities: User, League, Team, Player, Matchup, Recommendation, NewsItem, Transaction, AnalysisEngine
3. Loaded contracts/ → CLI interface commands, ESPN API integration
4. Generated 45 tasks across 5 phases following TDD methodology
5. Marked parallel tasks [P] based on file independence
6. Ordered by dependencies: Setup → Tests → Implementation → Integration → Polish
```

**Branch**: `001-fantasy-football-intelligent` | **Generated**: 2025-09-26

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Structure (Single Project - Extended espn_api)
```
ff_advisor/               # New fantasy advisor package
├── core/                # Core recommendation logic
├── ai/                  # AI/ML components (Ollama integration)
├── data/                # Database models and repositories
├── integrations/        # External service adapters (ESPN, news)
├── cli/                 # CLI commands
└── utils/               # Shared utilities

tests/
├── contract/           # Contract tests for external APIs
├── integration/        # Full workflow integration tests
└── unit/              # Unit tests for components
```

## Phase 3.1: Setup & Infrastructure

- [ ] T001 Create ff_advisor package structure following constitutional Library-First principle
- [ ] T002 Configure Python 3.11+ dependencies: FastAPI, Click, SQLAlchemy, Qdrant-client, Ollama, pytest
- [ ] T003 [P] Set up PostgreSQL database with Docker Compose for development
- [ ] T004 [P] Set up Qdrant vector database with Docker Compose for development  
- [ ] T005 [P] Configure linting (black, flake8, mypy) and pre-commit hooks
- [ ] T006 [P] Set up pytest configuration with async testing and testcontainers

## Phase 3.2: Contract Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**

### ESPN API Contract Tests [P]
- [ ] T007 [P] ESPN authentication contract test in tests/contract/test_espn_auth.py
- [ ] T008 [P] ESPN league data contract test in tests/contract/test_espn_league.py
- [ ] T009 [P] ESPN team roster contract test in tests/contract/test_espn_roster.py
- [ ] T010 [P] ESPN player stats contract test in tests/contract/test_espn_players.py
- [ ] T011 [P] ESPN matchup data contract test in tests/contract/test_espn_matchups.py

### CLI Interface Contract Tests [P]
- [ ] T012 [P] CLI auth commands contract test in tests/contract/test_cli_auth.py
- [ ] T013 [P] CLI lineup commands contract test in tests/contract/test_cli_lineup.py
- [ ] T014 [P] CLI roster commands contract test in tests/contract/test_cli_roster.py
- [ ] T015 [P] CLI trade commands contract test in tests/contract/test_cli_trade.py
- [ ] T016 [P] CLI waiver commands contract test in tests/contract/test_cli_waiver.py
- [ ] T017 [P] CLI watch commands contract test in tests/contract/test_cli_watch.py

### Integration Tests [P]
- [ ] T018 [P] User authentication and league setup integration test in tests/integration/test_user_onboarding.py
- [ ] T019 [P] Weekly lineup recommendation generation integration test in tests/integration/test_lineup_flow.py
- [ ] T020 [P] Trade analysis workflow integration test in tests/integration/test_trade_analysis.py
- [ ] T021 [P] Waiver wire recommendation integration test in tests/integration/test_waiver_flow.py
- [ ] T022 [P] News monitoring and notification integration test in tests/integration/test_news_pipeline.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)

### Data Models [P]
- [ ] T023 [P] User model with ESPN authentication in ff_advisor/data/models/user.py
- [ ] T024 [P] League model with ESPN settings in ff_advisor/data/models/league.py
- [ ] T025 [P] Team model with roster tracking in ff_advisor/data/models/team.py
- [ ] T026 [P] Player model with stats and projections in ff_advisor/data/models/player.py
- [ ] T027 [P] Matchup model with opponent analysis in ff_advisor/data/models/matchup.py
- [ ] T028 [P] Recommendation model with confidence scoring in ff_advisor/data/models/recommendation.py
- [ ] T029 [P] NewsItem model with source tracking in ff_advisor/data/models/news_item.py
- [ ] T030 [P] Transaction model with decision tracking in ff_advisor/data/models/transaction.py
- [ ] T031 [P] AnalysisEngine model with ML metadata in ff_advisor/data/models/analysis_engine.py

### Repository Layer [P]
- [ ] T032 [P] User repository with encrypted credential storage in ff_advisor/data/repositories/user_repository.py
- [ ] T033 [P] League repository with ESPN sync in ff_advisor/data/repositories/league_repository.py
- [ ] T034 [P] Player repository with vector embeddings in ff_advisor/data/repositories/player_repository.py

### ESPN Integration Service
- [ ] T035 ESPN API client with authentication in ff_advisor/integrations/espn/client.py
- [ ] T036 ESPN data synchronization service in ff_advisor/integrations/espn/sync_service.py
- [ ] T037 ESPN player stats aggregation in ff_advisor/integrations/espn/stats_service.py

### Core Business Logic
- [ ] T038 Recommendation engine core algorithms in ff_advisor/core/recommendation_engine.py
- [ ] T039 Lineup optimization service in ff_advisor/core/lineup_optimizer.py
- [ ] T040 Trade value analysis service in ff_advisor/core/trade_analyzer.py

## Phase 3.4: AI & Advanced Features

### AI/ML Integration
- [ ] T041 Ollama client for local AI inference in ff_advisor/ai/ollama_client.py
- [ ] T042 Player similarity embedding service in ff_advisor/ai/similarity_service.py  
- [ ] T043 News sentiment analysis pipeline in ff_advisor/ai/news_analyzer.py

### CLI Commands (Constitutional Requirement)
- [ ] T044 CLI authentication commands in ff_advisor/cli/auth_commands.py
- [ ] T045 CLI lineup management commands in ff_advisor/cli/lineup_commands.py
- [ ] T046 CLI trade analysis commands in ff_advisor/cli/trade_commands.py

## Phase 3.5: Integration & Infrastructure

### Database Integration
- [ ] T047 PostgreSQL connection and migration setup in ff_advisor/data/database.py
- [ ] T048 Qdrant vector store connection in ff_advisor/ai/vector_store.py
- [ ] T049 Database seeding with NFL player data in ff_advisor/data/seeds/

### Background Processing
- [ ] T050 News monitoring background tasks in ff_advisor/integrations/news/monitor.py
- [ ] T051 Notification service with email delivery in ff_advisor/integrations/notifications/service.py

### Error Handling & Logging
- [ ] T052 Structured logging configuration (Constitutional Observability) in ff_advisor/utils/logging.py
- [ ] T053 ESPN API error handling and fallback to Playwright in ff_advisor/integrations/espn/fallback.py

## Phase 3.6: Polish & Validation

### Unit Tests [P]
- [ ] T054 [P] Recommendation engine unit tests in tests/unit/test_recommendation_engine.py
- [ ] T055 [P] Trade analyzer unit tests in tests/unit/test_trade_analyzer.py
- [ ] T056 [P] ESPN client unit tests with mocking in tests/unit/test_espn_client.py

### Performance & Security
- [ ] T057 Performance testing for <5 minute recommendation requirement in tests/performance/
- [ ] T058 Security audit for ESPN credential encryption in ff_advisor/utils/security.py

### Documentation [P]
- [ ] T059 [P] API documentation generation in docs/api.md
- [ ] T060 [P] CLI usage documentation in docs/cli.md
- [ ] T061 [P] User guide updates in README.md

## Dependencies

### Critical Path
- Setup (T001-T006) → All other phases
- Contract Tests (T007-T022) → All implementation tasks
- Data Models (T023-T031) → Repositories (T032-T034) → Services (T035-T043)
- ESPN Integration (T035-T037) → Recommendation Engine (T038-T040)
- Core Logic (T038-T040) → CLI Commands (T044-T046)

### Parallel Opportunities
```bash
# Phase 3.2 - All contract tests can run simultaneously:
Task: "ESPN authentication contract test in tests/contract/test_espn_auth.py"
Task: "ESPN league data contract test in tests/contract/test_espn_league.py"  
Task: "CLI auth commands contract test in tests/contract/test_cli_auth.py"
# ... (all 16 contract tests)

# Phase 3.3 - All data models can run simultaneously:
Task: "User model with ESPN authentication in ff_advisor/data/models/user.py"
Task: "League model with ESPN settings in ff_advisor/data/models/league.py"
# ... (all 9 entity models)
```

## Constitutional Compliance Checkpoints

### Library-First Verification
- T001: ff_advisor package structure with clear library boundaries
- T023-T031: Self-contained model libraries
- T035-T043: Independently testable service libraries

### CLI Interface Verification  
- T044-T046: All functionality exposed via CLI commands
- T012-T017: Contract tests verify text-based input/output

### Test-First Verification
- T007-T022: All contract tests written before implementation
- T054-T056: Comprehensive unit test coverage

### Integration Testing Verification
- T018-T022: Critical integration points tested
- T047-T051: External service integrations covered

### Observability Verification
- T052: Structured logging implementation
- T057: Performance monitoring and validation

## Task Generation Rules Applied

✅ **Each contract file → contract test task marked [P]**: 16 contract tests (T007-T022)
✅ **Each entity in data-model → model creation task marked [P]**: 9 entity models (T023-T031)  
✅ **Each CLI command → implementation task**: 3 command groups (T044-T046)
✅ **Different files = parallel [P]**: All models, contract tests, unit tests marked [P]
✅ **Same file = sequential**: ESPN integration tasks (T035-T037) sequential
✅ **TDD ordering**: Tests (T007-T022) before implementation (T023+)

## Immediate Next Steps

1. **Execute T001-T006**: Set up development environment
2. **Execute T007-T022**: Write all contract tests (must fail initially)  
3. **Execute T023-T031**: Implement data models to make tests pass
4. **Continue sequential execution** following dependency order

**Ready for Implementation**: ✅ All 61 tasks defined with clear acceptance criteria and dependencies