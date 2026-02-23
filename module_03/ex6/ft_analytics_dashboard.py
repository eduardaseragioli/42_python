def main() -> None:
    """
    Analyze game player data using list, dict, and set comprehensions.
    """
    players: list[dict[str, any]] = [
        {"name": "alice", "scores": 2300, "achievements": [
            "first_kill", "speed_demon", "treasure_hunter",
            "collector", "perfectionist"], "active_regions": "north",
         "active": "active"},
        {"name": "bob", "scores": 1800, "achievements": [
            "level_10", "perfectionist", "treasure_hunter"],
         "active_regions": "east", "active": "active"},
        {"name": "charlie", "scores": 2150, "achievements": [
            "boss_slayer", "perfectionist", "treasure_hunter",
            "speed_demon", "collector", "perfectionist", "speed_demon"],
         "active_regions": "central", "active": "active"},
        {"name": "diana", "scores": 2050, "achievements": [
            "speed_demon"], "active_regions": "north", "active": "inative"}
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers: list[str] = [p["name"] for p in players
                               if p["scores"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled: list[int] = [p["scores"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = [p["name"] for p in players
                                 if p["active"] == "active"]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores: dict[str, int] = {p["name"]: p["scores"]
                                     for p in players[:3]}
    print(f"Player scores: {player_scores}")

    score: list[int] = [p["scores"] for p in players]
    score_categories: dict[str, int] = {
        "high": len([p for p in score if p > 2100]),
        "medium": len([p for p in score if 1900 <= p <= 2100]),
        "low": len([p for p in score if p < 1900])
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {p["name"]: len(p["achievements"])
                                          for p in players[:3]}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    all_achievements_list: list[str] = [achievement for p in players
                                        for achievement in p["achievements"]]
    unique_achievements: set[str] = {p for p in all_achievements_list
                                     if all_achievements_list.count(p) == 1}
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {p["active_regions"] for p in players}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players: int = len(players)
    print(f"Total players: {total_players}")

    total_achievements: int = len(all_achievements_list)
    print(f"Total unique achievements: {total_achievements}")

    scores: list[int] = [p["scores"] for p in players]
    average_score: float = sum(scores)/len(scores)
    print(f"Average score: {average_score}")

    top_performer: dict[str, any] | None = None
    for player in players:
        if (top_performer is None or
                player["scores"] > top_performer["scores"]):
            top_performer = player

    top_performer_str: str = (f"{top_performer['name']} "
                              f"({top_performer['scores']} points, "
                              f"{len(top_performer['achievements'])} "
                              f"achievements)")
    print(f"Top performer: {top_performer_str}")


if __name__ == "__main__":
    main()
