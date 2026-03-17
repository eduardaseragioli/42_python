"""Combat interface for cards that can attack and defend."""

from abc import ABC, abstractmethod


class Combatable(ABC):
    """Defines mandatory combat behavior."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Execute an attack against a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Handle incoming damage and return defense results."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return combat-related statistics."""
        pass
