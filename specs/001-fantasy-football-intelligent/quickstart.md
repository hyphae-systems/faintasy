# Quickstart: Fantasy Football Intelligent Advisor

**Generated**: 2025-09-26  
**Target Audience**: Novice fantasy football players  

## Getting Started in 5 Minutes

### Step 1: Installation and Setup
```bash
# Install the fantasy advisor
pip install fantasy-advisor

# Set up your ESPN league connection  
ff-advisor auth login \
  --league-id YOUR_LEAGUE_ID \
  --espn-s2 "YOUR_ESPN_S2_COOKIE" \
  --swid "YOUR_SWID_VALUE"

# Verify connection
ff-advisor auth status
```

**Expected Output**: "✅ Connected to [League Name] as [Your Team Name]"

### Step 2: Get Your First Recommendations  
```bash
# See this week's lineup suggestions
ff-advisor lineup suggest

# Check available free agents worth picking up
ff-advisor waiver suggest --position RB
```

**Expected Output**: 
- Start/sit recommendations with clear explanations
- Top waiver wire targets with projected value

### Step 3: Monitor Your Team
```bash  
# Add key players to your watchlist
ff-advisor watch add "Saquon Barkley" --reason "injury monitor"

# Set up notifications for important updates
ff-advisor notify config \
  --email your-email@example.com \
  --push-enabled true \
  --injury-alerts high
```

**Expected Output**: Confirmation that monitoring is active

## Essential Commands for New Users

### Weekly Lineup Management
```bash
# Every week before lineup lock (usually Sunday AM)
ff-advisor lineup suggest --confidence high

# Check if any of your players are injured
ff-advisor injuries --my-team

# See last-minute news that might affect your lineup  
ff-advisor news --my-players --since 4h
```

### Waiver Wire and Free Agency
```bash
# Tuesday mornings (waiver wire day)
ff-advisor waiver suggest --budget 25

# Throughout the week for streaming options
ff-advisor free-agents search --position K --available-only
```

### Trade Analysis
```bash
# When you receive a trade offer
ff-advisor trade analyze \
  --give "Your Player" \
  --receive "Their Player"

# When looking for trade partners  
ff-advisor trade suggest --need WR --have RB
```

## Understanding the Output

### Recommendation Confidence Levels
- **🟢 High**: Strong data support, clear advantage
- **🟡 Medium**: Good reasoning but some uncertainty  
- **🔴 Low**: Limited data or close decision

### Player Status Icons
- **✅**: Healthy and starting
- **⚠️**: Questionable or limited practice
- **❌**: Injured or unlikely to play
- **📈**: Trending up in value/usage  
- **📉**: Trending down in value/usage

### Trade Value Scores
- **Win (70-100)**: Great trade for you
- **Fair (40-69)**: Reasonable trade
- **Loss (0-39)**: Poor trade value

## Fantasy Football Basics for Beginners

### Scoring Systems
- **Standard**: Touchdowns and yardage only
- **PPR**: +1 point per reception (helps RBs/WRs)
- **Half-PPR**: +0.5 points per reception

### Key Positions by Priority
1. **QB**: Consistent but later draft picks often fine
2. **RB**: Scarcest position, draft early and often
3. **WR**: Deep position but elite ones are valuable
4. **TE**: Very thin after top tier
5. **K/DEF**: Stream based on matchups

### Weekly Strategy
- **Sunday-Tuesday**: Review results, process waiver claims
- **Wednesday-Saturday**: Monitor news, plan lineup changes
- **Sunday AM**: Set final lineup before games start

## Troubleshooting Common Issues

### Authentication Problems
```bash
# If login fails
ff-advisor auth login --verbose  # Shows detailed error info

# Private league access issues  
ff-advisor sync --force  # Refresh all data
```

### Missing Recommendations
```bash
# If no lineup suggestions appear
ff-advisor roster analyze  # Check if team data loaded properly

# Force data refresh
ff-advisor sync --league-only
```

### Notification Issues  
```bash
# Test notifications
ff-advisor notify test --type injury

# Check current settings
ff-advisor config get notifications
```

## Advanced Features (Once Comfortable)

### Custom Watchlists
```bash
# Monitor specific player types
ff-advisor watch add "Handcuff RBs" --auto-suggest
ff-advisor watch add "Injury Replacements" --auto-suggest
```

### League Analysis
```bash  
# Understand your competition
ff-advisor league power-rankings

# Find trade partners
ff-advisor league analyze --trade-needs
```

### Historical Performance
```bash
# Review your decision accuracy
ff-advisor history recommendations --success-rate

# See which advice types work best for you
ff-advisor history analyze --by-category
```

## Getting Help

### Built-in Help
```bash
# General help
ff-advisor --help

# Command-specific help  
ff-advisor lineup --help
ff-advisor trade analyze --help
```

### Common Use Cases
- **Sunday Morning**: `ff-advisor lineup suggest --confidence high`
- **Tuesday Waivers**: `ff-advisor waiver suggest`  
- **Trade Deadline**: `ff-advisor trade suggest --aggressive`
- **Playoff Push**: `ff-advisor roster analyze --playoffs`

### Emergency Situations
- **Player Injured During Game**: `ff-advisor injuries "Player Name" --replacements`
- **Late Scratch**: `ff-advisor free-agents search --position QB --kickoff-soon`
- **Bye Week Hell**: `ff-advisor lineup suggest --fill-holes`

## Next Steps

1. **Week 1**: Use basic lineup suggestions and waiver recommendations
2. **Week 2-4**: Start analyzing trades and monitoring news
3. **Week 5+**: Leverage advanced features and historical insights  
4. **Playoffs**: Focus on matchup analysis and roster optimization

The advisor learns from your decisions over time, so the more you use it and provide feedback, the better it becomes at understanding your preferences and league dynamics.