# ESPN API Contract

**Service**: ESPN Fantasy Football API Integration  
**Version**: 1.0  
**Generated**: 2025-09-26

## Authentication Contract

```yaml
endpoint: authenticate
method: POST
input:
  espn_s2: string (required) - ESPN S2 cookie
  swid: string (required) - ESPN SWID cookie  
  league_id: integer (required) - ESPN league identifier
output:
  success:
    authenticated: boolean
    user_info:
      user_id: string
      display_name: string
      team_id: integer
    league_access: boolean
  error:
    error_code: string
    message: string
    retry_after: integer (optional)
```

## League Data Contract

```yaml
endpoint: get_league_info
method: GET
input:
  league_id: integer (required)
  season_year: integer (required)
output:
  success:
    league:
      id: integer
      name: string
      season_year: integer
      size: integer
      scoring_format: enum[standard, ppr, half_ppr, custom]
      current_week: integer
      playoff_start_week: integer
      trade_deadline_week: integer
      settings:
        roster_slots: object
        scoring_rules: object
        waiver_type: string
    teams: array
      - team_id: integer
        team_name: string
        owner: string
        record: object
        roster: array[player_objects]
  error:
    error_code: string
    message: string
```

## Player Data Contract

```yaml
endpoint: get_player_info
method: GET
input:
  player_id: integer (required)
  season_year: integer (required)
  week: integer (optional)
output:
  success:
    player:
      id: integer
      name: string
      position: enum[QB, RB, WR, TE, K, DEF]
      team: string
      bye_week: integer
      injury_status: enum[active, questionable, doubtful, out, ir]
      projected_points: number
      season_stats: object
      ownership_percent: number
      average_points: number
  error:
    error_code: string
    message: string
```

## Roster Management Contract

```yaml
endpoint: get_team_roster
method: GET
input:
  team_id: integer (required)
  week: integer (optional, defaults to current)
output:
  success:
    roster:
      starting_lineup: array[player_objects]
      bench: array[player_objects]
      injured_reserve: array[player_objects]
    lineup_locked: boolean
    roster_changes_remaining: integer
  error:
    error_code: string
    message: string
```

## Free Agents Contract

```yaml
endpoint: get_free_agents  
method: GET
input:
  league_id: integer (required)
  position: enum[QB, RB, WR, TE, K, DEF] (optional)
  size: integer (optional, max 100)
output:
  success:
    available_players: array
      - player_id: integer
        name: string
        position: string
        team: string
        projected_points: number
        percent_owned: number
        avg_points: number
        recent_news: string (optional)
  error:
    error_code: string
    message: string
```

## Error Handling

**Rate Limiting**:
- Max 100 requests per minute
- HTTP 429 response with Retry-After header
- Exponential backoff required

**Authentication Errors**:
- HTTP 401: Invalid or expired credentials  
- HTTP 403: Private league access denied
- HTTP 404: League not found

**Data Consistency**:
- All timestamps in ISO 8601 format
- Player IDs consistent across endpoints
- Null handling for optional fields
- Graceful degradation when partial data available

## Integration Notes

- ESPN API updates in real-time during games
- Historical data available for completed seasons
- Private leagues require valid S2/SWID cookies
- Public leagues accessible without authentication
- Some endpoints may be temporarily unavailable during ESPN maintenance