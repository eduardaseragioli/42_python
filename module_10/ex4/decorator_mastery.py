from collections.abc import Callable
import functools
from functools import wraps
from typing import Any
import time

def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any: 
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get('power', None)
            if power is None:
                power = args[1] if len(args) > 1 and not isinstance(args[0], int) else args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying...  (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator
                    

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if all(char.isalpha() or char.isspace() for char in name):
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"
    
    result = fireball()
    print(f"Result: {result}")
    
    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception("Spell failed!")
    print(unstable_spell())

 
    @retry_spell(3)
    def stable_spell() -> str:
        return "Waaaaaaagh spelled !"
    print(stable_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("M3"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))

if __name__ == "__main__":
    main()