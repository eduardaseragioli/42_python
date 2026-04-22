from collections.abc import Callable

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(fireball, 3)
    original = fireball("Dragon", 10)
    amplified = mega("Dragon", 10)
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    def condition(target: str, power: int) -> bool:
        return power >= 50
    conditional = conditional_caster(condition, fireball)
    print(conditional("Dragon", 100))
    print(conditional("Dragon", 10))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    results = sequence("Dragon", 20)
    for result in results:
        print(f"{result}")


if __name__ == "__main__":
    main()