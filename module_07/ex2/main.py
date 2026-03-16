from ex2.EliteCard import EliteCard
from ex2.Magical import Magical
from ex2.Combatable import Combatable

def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    method_card: list = ['play', 'get_card_info', 'is_playable']
    method_com: list = ['attack', 'defend', 'get_combat_stats']
    method_magic: list = ['cast_spell', 'channel_mana', 'get_magic_stats']

    print(f"- Card: {method_card}")
    print(f"- Combatable: {method_com}")
    print(f"- Magical: {method_magic}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    arcane_card = EliteCard('Arcane Warrior', 5, 'Legendary', 5, 10, 5, 4)

    target = {"name": "Enemy", "health": 10}

    print("Combat phase:")
    print(f"Attack result: {arcane_card.attack(target)}")
    print(f"Defense result: {arcane_card.defend(5)}")

    print("\nMagic phase:")
    targets: list = ["Enemy1", "Enemy2"]
    print(f"Spell cast: {arcane_card.cast_spell('Fireball', targets)}")
    print(f"Mana channel: {arcane_card.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
if __name__ == "__main__":
    main()