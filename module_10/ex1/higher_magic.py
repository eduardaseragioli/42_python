from collections.abc import Callable

def spell(target: str, power: int) -> str:

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)
    return combined

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)
    return amplifier

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def  caster(target: str, power: int) -> Callable:
        if condition

def spell_sequence(spells: list[Callable]) -> Callable: