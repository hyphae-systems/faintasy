# CLI Interface Contract

**Service**: Fantasy Advisor Command Line Interface  
**Version**: 1.0  
**Generated**: 2025-09-26

## Authentication Commands

### Login
```bash
ff-advisor auth login --league-id 12345 --espn-s2 "cookie_value" --swid "swid_value"
```
**Input**: ESPN credentials and league ID  
**Output**: Authentication confirmation, saved credentials  
**Exit Codes**: 0 (success), 1 (invalid credentials), 2 (network error)

### Status  
```bash
ff-advisor auth status [--json]
```
**Input**: None (uses saved credentials)  
**Output**: Current authentication status and league access  
**Format**: Human-readable or JSON

## Team Analysis Commands

### Lineup Recommendations
```bash
ff-advisor lineup suggest [--week 8] [--confidence high] [--json]
```
**Input**: Optional week number and confidence filter  
**Output**: Start/sit recommendations with reasoning  
**Format**: Table with player names, positions, recommendations, and explanations

### Roster Analysis  
```bash
ff-advisor roster analyze [--depth-chart] [--json]
```
**Input**: None (analyzes user's team)  
**Output**: Team strengths, weaknesses, and depth analysis  
**Format**: Structured analysis with actionable insights

## Transaction Commands

### Trade Analysis
```bash
ff-advisor trade analyze --give "Player A" --receive "Player B" [--json]
ff-advisor trade suggest [--position QB] [--need RB] [--json]
```
**Input**: Trade players or position needs  
**Output**: Trade value assessment and recommendations  
**Format**: Detailed analysis with fairness score and projections

### Waiver Wire  
```bash
ff-advisor waiver suggest [--position RB] [--budget 50] [--json]
```
**Input**: Position filter and FAAB budget (if applicable)  
**Output**: Prioritized pickup recommendations  
**Format**: Ranked list with ownership %, projections, and rationale

### Free Agents
```bash
ff-advisor free-agents search [--position WR] [--available-only] [--json]  
```
**Input**: Position filter and availability  
**Output**: Available players sorted by value  
**Format**: Table with player info, projections, and recommendation score

## News and Updates Commands

### Player News
```bash
ff-advisor news player "Patrick Mahomes" [--since 24h] [--json]
ff-advisor news team "Kansas City Chiefs" [--json]
```
**Input**: Player name or team with time filter  
**Output**: Recent news affecting fantasy value  
**Format**: Chronological list with impact assessment

### Injury Report
```bash  
ff-advisor injuries [--my-team] [--position QB] [--severity high] [--json]
```
**Input**: Scope and severity filters  
**Output**: Current injury status and fantasy impact  
**Format**: Table with player, status, expected return, replacement suggestions

## Monitoring Commands

### Watchlist
```bash
ff-advisor watch add "Player Name" [--reason "handcuff"]
ff-advisor watch list [--json]  
ff-advisor watch remove "Player Name"
```
**Input**: Player names and optional reason  
**Output**: Confirmation and current watchlist  
**Format**: Simple list with monitoring reasons

### Notifications
```bash
ff-advisor notify config --email user@example.com --push-enabled true
ff-advisor notify test [--type injury] [--type trade]
```  
**Input**: Notification preferences and test types  
**Output**: Configuration confirmation and test notifications  
**Format**: Settings summary

## League Commands

### Standings
```bash
ff-advisor league standings [--json]
ff-advisor league schedule [--week 8] [--json]
```
**Input**: Optional week filter  
**Output**: Current standings or weekly matchups  
**Format**: Table with team names, records, and upcoming opponents

### Power Rankings
```bash  
ff-advisor league power-rankings [--algorithm standard] [--json]
```
**Input**: Optional ranking algorithm  
**Output**: Teams ranked by projected strength  
**Format**: Ranked list with strength scores and explanations

## Data and Configuration Commands

### Sync
```bash
ff-advisor sync [--force] [--league-only]
```
**Input**: Force flag for complete refresh  
**Output**: Sync status and data freshness  
**Exit Codes**: 0 (success), 1 (partial failure), 2 (complete failure)

### Config
```bash
ff-advisor config get [setting_name]
ff-advisor config set setting_name value
ff-advisor config reset [--all]
```
**Input**: Setting names and values  
**Output**: Current configuration or confirmation  
**Format**: Key-value pairs

## Global Options

**All commands support**:
- `--json`: Output in JSON format for scripting
- `--verbose`: Detailed logging and debug information  
- `--help`: Command-specific help and examples
- `--version`: Display version information

## Input/Output Standards

**Input**:
- Arguments via command line flags
- Configuration from files (~/.ff-advisor/config.yaml)
- Credentials from secure storage

**Output**:  
- Human-readable tables and summaries (default)
- JSON format for programmatic use (--json flag)
- Structured logging to stderr for debugging
- Progress indicators for long-running operations

**Error Handling**:
- Exit code 0 for success
- Exit code 1 for user errors (invalid input, authentication)
- Exit code 2 for system errors (network, database)
- Clear error messages with suggested solutions
- Graceful handling of partial data scenarios

## Performance Expectations

- Commands complete within 5 seconds for cached data
- Real-time data fetching may take up to 15 seconds  
- Bulk operations show progress indicators
- Concurrent command execution supported
- Offline mode available for cached data