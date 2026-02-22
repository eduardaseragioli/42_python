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
            "speed_demon"], "active_regions": "north", "active": "inative"}
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

    score = [p["scores"] for p in players]
    score_categories = {
        "high": len([p for p in score if p > 2100]),
        "medium": len([p for p in score if 1900 <= p <= 2100]),
        "low": len([p for p in score if p < 1900])
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players[:3]}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    all_achievements_list = [achievement for p in players for achievement in p["achievements"]]
    unique_achievements = {p for p in all_achievements_list if all_achievements_list.count(p) == 1}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["active_regions"] for p in players}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    print(f"Total players: {total_players}")

    total_achievements = len(all_achievements_list)
    print(f"Total unique achievements: {total_achievements}")

    scores = [p["scores"] for p in players]
    average_score = sum(scores)/len(scores)
    print(f"Average score: {average_score}")

    top_performer = None
    for player in players:
        if top_performer is None or player["scores"] > top_performer["scores"]:
            top_performer = player

    top_performer_str = f"{top_performer["name"]} ({top_performer["scores"]} points, {len(top_performer["achievements"])} achievements)"
    print(f"Top performer: {top_performer_str}")

    


if __name__ == "__main__":
    main()
