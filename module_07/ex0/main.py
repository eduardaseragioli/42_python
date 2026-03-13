from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    fire = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )
    info_card = fire.get_card_info()
    print(f"CreatureCard Info: \n{info_card}")

    print(f"\nPlaying {fire.name} with 6 mana available:")
    game_state: dict = {"active_creatures": []}
    print(f"Playable: {fire.is_playable(6)}")
    print(f"Play result: {fire.play(game_state)}")

    goblin = {
        "name": "Goblin Warrior",
        "health": 3
    }
    print(f"\n{fire.name} attacks {goblin['name']}:")
    attack_result = fire.attack_target(goblin)
    print(f"Attack result: {attack_result}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
