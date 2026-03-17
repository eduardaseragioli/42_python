"""Base abstract card model used across module_07."""

from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    """Abstract base class for all card types."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize common card attributes."""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Apply this card effect to the current game state."""
        pass

    def get_card_info(self) -> dict:
        """Return common card metadata."""
        card_info: dict[str, Any] = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': type(self).__name__
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        """Check if available mana can pay this card cost."""
        return available_mana >= self.cost
