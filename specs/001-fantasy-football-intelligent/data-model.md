# Data Model: Fantasy Football Intelligent Advisor

**Phase 1 Output** | **Generated**: 2025-09-26

## Core Entities

### User
**Purpose**: Represents a fantasy football player using the advisor system  
**Key Attributes**:
- `id`: Unique identifier
- `email`: User email address
- `espn_s2_cookie`: ESPN authentication token (encrypted)
- `espn_swid`: ESPN user identifier (encrypted)
- `notification_preferences`: JSON config for alerts
- `experience_level`: ENUM (novice, intermediate, advanced)
- `created_at`: Account creation timestamp
- `last_active`: Last system interaction

**Relationships**:
- One-to-many with League (user can be in multiple leagues)
- One-to-many with Recommendation (user receives many recommendations)
- One-to-many with UserDecision (tracks user choices)

### League
**Purpose**: ESPN fantasy football league instance with settings and participants  
**Key Attributes**:
- `id`: Unique system identifier  
- `espn_league_id`: ESPN's league identifier
- `name`: League display name
- `season_year`: Fantasy season (e.g., 2024)
- `scoring_format`: ENUM (standard, ppr, half_ppr, custom)
- `team_count`: Number of teams (8-16)
- `playoff_start_week`: When playoffs begin
- `trade_deadline`: Last week for trades
- `waiver_type`: ENUM (faab, rolling, reverse_standings)
- `is_active`: Whether league is currently running
- `settings_json`: Custom league rules and scoring

**Relationships**:
- Many-to-one with User (user owns/manages)
- One-to-many with Team (league contains multiple teams)
- One-to-many with Matchup (weekly league matchups)

### Team
**Purpose**: User's fantasy team within a specific league  
**Key Attributes**:
- `id`: Unique identifier
- `league_id`: Reference to parent league
- `user_id`: Team owner
- `espn_team_id`: ESPN's team identifier
- `team_name`: Custom team name
- `current_record`: Wins-losses-ties
- `total_points`: Season point total
- `current_rank`: League standing position
- `roster_json`: Current player roster
- `lineup_json`: Active starting lineup
- `bench_json`: Bench players
- `ir_json`: Injured reserve players

**Relationships**:
- Many-to-one with League
- Many-to-one with User  
- One-to-many with Transaction (team makes roster moves)
- Many-to-many with Player (through roster relationships)

### Player
**Purpose**: NFL player eligible for fantasy football  
**Key Attributes**:
- `id`: Unique system identifier
- `espn_player_id`: ESPN's player identifier
- `name`: Player full name
- `position`: ENUM (QB, RB, WR, TE, K, DEF)
- `nfl_team`: Current NFL team
- `bye_week`: Week player's team is off
- `injury_status`: ENUM (healthy, questionable, doubtful, out, ir)
- `season_stats_json`: Accumulated statistics
- `weekly_projections_json`: Projected points
- `adp`: Average draft position
- `ownership_percentage`: Roster percentage across leagues
- `last_news_update`: Timestamp of latest news
- `fantasy_relevance_score`: Computed relevance rating

**Relationships**:
- One-to-many with NewsItem (player generates news)
- One-to-many with PlayerEmbedding (similarity vectors)
- Many-to-many with Team (through roster relationships)

### Matchup
**Purpose**: Weekly fantasy matchup between two teams  
**Key Attributes**:
- `id`: Unique identifier
- `league_id`: Parent league
- `week_number`: NFL week (1-18)
- `team_a_id`: First team
- `team_b_id`: Second team  
- `team_a_projected`: Projected points for team A
- `team_b_projected`: Projected points for team B
- `team_a_actual`: Final points for team A (nullable until complete)
- `team_b_actual`: Final points for team B (nullable until complete)
- `is_complete`: Whether matchup finished
- `game_factors_json`: Weather, game flow, etc.

**Relationships**:
- Many-to-one with League
- References two Team entities

### Recommendation
**Purpose**: AI-generated advice for user actions  
**Key Attributes**:
- `id`: Unique identifier
- `user_id`: Target user
- `team_id`: Relevant team
- `type`: ENUM (lineup, trade, waiver, drop, general)
- `priority`: ENUM (low, medium, high, urgent)
- `confidence_level`: ENUM (low, medium, high)
- `title`: Brief recommendation summary
- `reasoning`: Detailed explanation
- `supporting_data_json`: Analysis details
- `recommended_action`: Specific action to take
- `created_at`: When generated
- `expires_at`: When recommendation becomes stale
- `user_response`: ENUM (accepted, rejected, ignored, pending)

**Relationships**:
- Many-to-one with User
- Many-to-one with Team
- May reference specific Player entities

### NewsItem
**Purpose**: NFL news affecting player fantasy value  
**Key Attributes**:
- `id`: Unique identifier
- `player_id`: Affected player (nullable for general news)
- `headline`: News headline
- `content`: Full article content
- `source`: News source (ESPN, NFL.com, etc.)
- `source_reliability`: ENUM (tier1, tier2, tier3, social)
- `published_at`: Original publication time
- `impact_severity`: ENUM (low, medium, high, critical)
- `fantasy_implications`: How this affects fantasy value
- `sentiment_score`: AI-analyzed sentiment (-1 to 1)
- `processed_at`: When system analyzed the news

**Relationships**:
- Many-to-one with Player (when player-specific)
- One-to-many with NewsEmbedding (vector representations)

### Transaction
**Purpose**: Fantasy roster moves and their outcomes  
**Key Attributes**:
- `id`: Unique identifier
- `team_id`: Team making the move
- `transaction_type`: ENUM (add, drop, trade, lineup_change)
- `player_added_id`: Player acquired (nullable)
- `player_dropped_id`: Player released (nullable)
- `trade_details_json`: Full trade information
- `executed_at`: When transaction occurred
- `recommended_by_system`: Whether advisor suggested this
- `outcome_score`: Success rating after 2 weeks (nullable)
- `rationale`: Reason for the move

**Relationships**:
- Many-to-one with Team
- References Player entities for adds/drops

## Vector Embeddings Schema

### PlayerEmbedding
**Purpose**: Vector representations for player similarity analysis  
**Key Attributes**:
- `player_id`: Reference to Player
- `embedding_type`: ENUM (stats, news, similarity)  
- `vector`: High-dimensional embedding array
- `model_version`: AI model used for generation
- `created_at`: When embedding was generated

### NewsEmbedding  
**Purpose**: Vector representations for news content analysis
**Key Attributes**:
- `news_id`: Reference to NewsItem
- `embedding`: Content embedding vector
- `summary_embedding`: Headline embedding vector
- `model_version`: AI model used
- `created_at`: Generation timestamp

## Database Indexes

**Performance-Critical Indexes**:
- `users(email)` - User authentication
- `leagues(espn_league_id, season_year)` - League lookups
- `teams(league_id, user_id)` - User's teams per league  
- `players(espn_player_id)` - ESPN data sync
- `players(position, nfl_team)` - Filtering and search
- `news_items(player_id, published_at)` - Player news timeline
- `recommendations(user_id, created_at, priority)` - User feed
- `transactions(team_id, executed_at)` - Team history

## Data Relationships Summary

```
User (1) ──────── (M) League
  │                   │
  │                   │
  ▼                   ▼
Team (M) ────────── (1) League  
  │
  │
  ▼
Transaction
  │
  │
  ▼
Player ◄────── NewsItem
  │               │
  │               │
  ▼               ▼  
PlayerEmbedding   NewsEmbedding
```

## Schema Migration Strategy

1. **Initial Schema**: Core entities (User, League, Team, Player)
2. **Analytics Layer**: Recommendations, Transactions, News
3. **AI Enhancement**: Embeddings and vector operations
4. **Performance**: Indexes and optimization
5. **Extensions**: Custom scoring, advanced analytics

Each migration will be versioned and include rollback procedures following Prisma best practices.