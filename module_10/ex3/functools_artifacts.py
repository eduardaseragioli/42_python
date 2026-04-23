import operator
import functools
from functools import reduce, partial
from typing import Any
from collections.abc import Callable

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire")
    ice_enchant = partial(base_enchantment, power=50, element="ice")
    lightning_enchant = partial(base_enchantment, power=50, element="lightning")
    return {
        'fire': fire_enchant,
        'ice': ice_enchant,
        'lightning': lightning_enchant
    }

 
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable[[Any], str]:
    
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"
    
    @cast.register(int)
    def cast_int(spell: int) -> str:
        return f"{spell} damage"
    
    @cast.register(str)
    def cast_str(spell: str) -> str:
        return f"{spell}"
    
    @cast.register(list)
    def cast_list(spell: list) -> str:
        return f"{len(spell)} spells"

    return cast

def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(f"{dispatcher(3.14)}")

if __name__ == "__main__":
    main()