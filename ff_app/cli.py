import argparse
import sys

from espn_api.football.league import League


def summarize_week(league, week):
    box_scores = league.box_scores(week)
    lines = []
    for box in box_scores:
        home = next((t for t in league.teams if t.team_id == box.home_team), None)
        away = next((t for t in league.teams if t.team_id == box.away_team), None)
        home_name = home.team_name if home else 'BYE'
        away_name = away.team_name if away else 'BYE'
        lines.append(f"{away_name} {box.away_score} @ {home_name} {box.home_score} (proj: {box.away_projected:.1f}-{box.home_projected:.1f})")
    return "\n".join(lines)


def lineup_tips(league, week):
    tips = []
    scores = league.box_scores(week)
    for box in scores:
        for team_id, lineup in [(box.home_team, box.home_lineup), (box.away_team, box.away_lineup)]:
            team = next((t for t in league.teams if t.team_id == team_id), None)
            if not team:
                continue
            playable = [p for p in lineup if p.slot_position not in ('BE', 'IR', 'FA')]
            bench = [p for p in lineup if p.slot_position == 'BE']
            if not bench:
                continue
            for starter in playable:
                better = [b for b in bench if b.position == starter.position and b.projected_points > starter.projected_points + 1.0]
                if better:
                    best = sorted(better, key=lambda p: p.projected_points, reverse=True)[0]
                    delta = round(best.projected_points - starter.projected_points, 2)
                    tips.append(f"{team.team_name}: Consider starting {best.name} over {starter.name} (+{delta} proj)")
    return "\n".join(tips) or "No lineup suggestions this week."


def free_agent_suggestions(league, week, size):
    agents = league.free_agents(week=week, size=size)
    sorted_agents = sorted(agents, key=lambda p: (p.projected_points, p.percent_owned), reverse=True)[:10]
    lines = [f"{p.name} ({p.position}, {p.proTeam}) proj {p.projected_points:.1f}, owned {p.percent_owned}%" for p in sorted_agents]
    return "\n".join(lines) or "No free agents found."


def main(argv=None):
    parser = argparse.ArgumentParser(description='Fantasy Football Advisor')
    parser.add_argument('--league-id', type=int, required=True)
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--espn-s2', dest='espn_s2', default=None)
    parser.add_argument('--swid', dest='swid', default=None)
    parser.add_argument('--week', type=int, default=None)
    parser.add_argument('--fa-size', type=int, default=50)
    args = parser.parse_args(argv)

    league = League(league_id=args.league_id, year=args.year, espn_s2=args.espn_s2, swid=args.swid)
    week = args.week or league.current_week

    print("=== Weekly Scoreboard ===")
    print(summarize_week(league, week))
    print("\n=== Power Rankings ===")
    for rank, team in enumerate(league.power_rankings(week), start=1):
        print(f"{rank}. {team.team.team_name} (wins: {sum(1 for o in team.team.outcomes[:week] if o == 'W')})")
    print("\n=== Lineup Tips ===")
    print(lineup_tips(league, week))
    print("\n=== Free Agents ===")
    print(free_agent_suggestions(league, week, args.fa_size))


if __name__ == '__main__':
    main(sys.argv[1:])

