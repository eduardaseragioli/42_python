from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create philosopher's stone using transmutation and potion.

    Returns:
        str: Philosopher's stone creation result.
    """
    lead: str = lead_to_gold()
    healing: str = healing_potion()
    return f"Philosopher's stone created using {lead} and {healing}"


def elixir_of_life() -> str:
    """Create elixir of life for eternal youth.

    Returns:
        str: Elixir of life creation result.
    """
    return "Elixir of life: eternal youth achieved!"
