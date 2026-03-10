from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    """Demonstrate circular dependency avoidance using late imports."""

    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    air: str = validate_ingredients("fire air")
    print(f"validate_ingredients(\"fire air\"): {air}")

    scales: str = validate_ingredients("dragon scales")
    print(
        f"record_spell(\"Dark Magic\", \"shadow\"): {scales}")

    print("\nTesting spell recording with validation:")
    fire: str = record_spell("Fireball", "fire air")
    print(f"record_spell(\"Fireball\", \"fire air\"): {fire}")

    shadow: str = record_spell("Dark Magic", "shadow")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {shadow}")

    print("\nTesting late import technique:")
    ligh: str = record_spell("Lightning", "air")
    print(f"record_spell(\"Lightning\", \"air\"): {ligh}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
