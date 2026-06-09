#!/usr/bin/env python3


def ft_analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===")
    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "achievements": ["first_kill", "explorer", "level_10",
                             "boss_slayer", "pioneer", "winner"],
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "achievements": ["tank", "explorer", "novice", "winner", "mvp",
                             "godlike"],
            "region": "east"
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "achievements": ["pioneer", "speed_runner", "novice", "mvp",
                             "godlike", "healer", "tank", "tank"],
            "region": "north"
        },
        {
            "name": "diana",
            "score": 2000,
            "active": False,
            "achievements": ["first_kill"],
            "region": "central"
        }
    ]
    try:
        print("\n=== List Comprehension Examples ===")
        high_scorers = [p["name"] for p in players if p["score"] >= 2000]
        print(f"High scorers (>2000): {high_scorers}")
        scores_doubled = [p["score"] * 2 for p in players]
        print(f"Scores doubled: {scores_doubled}")
        active = [p["name"] for p in players if p["active"]]
        print(f"Active players: {active}")
        print("\n=== Dict Comprehension Examples ===")
        player_scores = {p["name"]: p["score"] for p in players if p["active"]}
        print(f"Player scores: {player_scores}")
        score_categories = {
                "high": len([p for p in players if p["score"] >= 2000]),
                "medium": len([p for p in players if 1800 <= p["score"] <=
                               2000]),
                "low": len([p for p in players if p["score"] <= 1800])}
        print(f"Score categories: {score_categories}")
        ach_counts = {p["name"]: len(set(p["achievements"])) for p in players
                      if p["active"]}
        print(f"Achievement counts: {ach_counts}")
        print("\n=== Set Comprehension Examples ===")
        unique_players = {p["name"] for p in players}
        print(f"Unique players: {unique_players}")
        unique_achievements = {ach for p in players for ach
                               in p["achievements"]}
        alice_set = {a for p in players if p["name"] == "alice"
                     for a in p["achievements"]}
        bob_set = {a for p in players if p["name"] == "bob"
                   for a in p["achievements"]}
        charlie_set = {a for p in players if p["name"] == "charlie"
                       for a in p["achievements"]}
        only_alice = alice_set.difference(bob_set.union(charlie_set))
        only_bob = bob_set.difference(alice_set.union(charlie_set))
        only_charlie = charlie_set.difference(alice_set.union(bob_set))
        rare = only_alice.union(only_bob).union(only_charlie)
        print(f"Unique achievements: {rare}")
        active_regions = {p["region"] for p in players}
        print(f"Active regions: {active_regions}")
        print("\n=== Combined Analysis ===")
        total_players = len(players)
        print(f"Total players: {total_players}")
        total_unique_ach = len(unique_achievements)
        print(f"Total unique achievements: {total_unique_ach}")
        avg_score = sum(p["score"] for p in players) / total_players
        print(f"Average score: {avg_score}")
        top = sorted([(p["score"], len(set(p["achievements"])), p["name"])
                      for p in players], reverse=True)[0]
        print(f"Top performer: {top[2]} ({top[0]} points, {top[1]}"
              f" achievements)")
    except KeyError as e:
        print(f"Error: Missing key {e}")
    except TypeError as e:
        print(f"Error: Invalid data type {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ft_analytics_dashboard()
