from .basic import lead_to_gold
from ..potions import healing_potion

def philosophers_stone() -> str:
    lead: str = lead_to_gold()
    healing: str = healing_potion()
    return f"Philosopher’s stone created using {lead} and {healing}"

def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"