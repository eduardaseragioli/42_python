import alchemy.transmutation as transmutation
from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life


def main() -> None:
    """Demonstrate absolute and relative import pathways."""
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    lead: str = lead_to_gold()
    stone: str = stone_to_gem()
    print(f"lead_to_gold(): {lead}")
    print(f"stone_to_gem(): {stone}")

    print("\nTesting Relative Imports (from advanced.py):")
    phi: str = philosophers_stone()
    elixir: str = elixir_of_life()
    print(f"philosophers_stone(): {phi}")
    print(f"elixir_of_life(): {elixir}")

    print("\nTesting Package Access:")
    lead_all = transmutation.lead_to_gold()
    phi_all = transmutation.philosophers_stone()
    print(f"alchemy.transmutation.lead_to_gold(): {lead_all}")
    print(f"alchemy.transmutation.philosophers_stone(): {phi_all}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
