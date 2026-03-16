from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    print("")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 1, 6)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 20, 80)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)
    interfacer = "[Card, Combatable, Rankable]"

    d_info = dragon.get_rank_info()
    print(f"{dragon.name}: (ID: {dragon_id}):")
    print(f"- Interfaces: {interfacer}")
    print(f"- Rating: {d_info['rating']}")
    print(f"- Record: {d_info['record']}")

    w_info = wizard.get_rank_info()
    print(f"\n{wizard.name}: (ID: {wizard_id}):")
    print(f"- Interfaces: {interfacer}")
    print(f"- Rating: {w_info['rating']}")
    print(f"- Record: {w_info['record']}")

    print("\nCreating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")

    print("Tournament Leaderboard:\n")
    leaderboard = platform.get_leaderboard()
    for c in leaderboard:
        record = f"{c['wins']}-{c['losses']}"
        print(
                f"{c['position']}. {c['name']}"
                f" - Rating: {c['rating']} ({record})"
            )

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
