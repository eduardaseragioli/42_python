"""Abstract factory interface for card creation families."""

from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Defines card factory contract for themed card sets."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card instance."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card instance."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card instance."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck grouped by card category."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Describe supported card archetypes."""
        pass
