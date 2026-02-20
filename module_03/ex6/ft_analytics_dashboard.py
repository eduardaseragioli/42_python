import math


def main() -> None:
    players = [
        {"name": "alice", "scores": 2300, "achievements": [
            "first_kill", "speed_demon", "treasure_hunter", "collector", "perfectionist"], "active_regions": "north", "active": "active"},
        {"name": "bob", "scores": 1800, "achievements": [
            "level_10", "perfectionist", "treasure_hunter"], "active_regions": "east", "active": "active"},
        {"name": "charlie", "scores": 2150, "achievements": ["boss_slayer", "perfectionist", "treasure_hunter",
                                                             "speed_demon", "collector", "perfectionist", "speed_demon"], "active_regions": "central", "active": "active"},
        {"name": "diana", "scores": 2050, "achievements": [
            "speed_demon"], "active_regions": "south", "active": "inative"}
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["scores"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["scores"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p["name"] for p in players if p["active"] == "active"]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["scores"] for p in players[:3]}
    print(f"Player scores: {player_scores}")

    #score_categories = {p}
    #print(f"Score categories: {}")

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players[:3]}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    all_achievements_list = [achievement for p in players for achievement in p["achievements"]]
    unique_achievements = {p for p in all_achievements_list if all_achievements_list.count(p) == 1}
    print(f"Unique achievements: {unique_achievements}")

    


if __name__ == "__main__":
    main()
