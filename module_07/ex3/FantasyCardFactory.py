"""Concrete card factory for fantasy-themed cards."""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Create fantasy creatures, spells, and artifacts."""

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature based on provided name or power."""
        if isinstance(name_or_power, str):
            return CreatureCard(name_or_power, 3, "Legendary", 3, 5)
        elif isinstance(name_or_power, int):
            return CreatureCard("Creature", 3, "Legendary",
                                name_or_power, name_or_power + 3)
        else:
            return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card based on provided name or power."""
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, 2, "Legendary", 5)
        elif isinstance(name_or_power, int):
            return SpellCard("Spell", 3, "Legendary", name_or_power)
        else:
            return SpellCard("Fireball", 3, "Common", 4)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card based on provided name or durability."""
        if isinstance(name_or_power, str):
            return ArtifactCard(name_or_power, 2, "Legendary", 3,
                                "+1 mana per turn")
        elif isinstance(name_or_power, int):
            return ArtifactCard("Artifact", 2, "Legendary",
                                name_or_power, "+1 mana per turn")
        else:
            return ArtifactCard("Mana Ring", 3, "Common", 2, "Restore 2 Mana")

    def create_themed_deck(self, size: int) -> dict:
        """Build a themed deck split into creatures, spells, and artifacts."""
        creature: list = []
        spell: list = []
        artifact: list = []

        num_creatures = size * 50 // 100
        num_spells = size * 30 // 100
        num_artifacts = size - num_creatures - num_spells

        for _ in range(num_creatures):
            creature.append(self.create_creature())

        for _ in range(num_spells):
            spell.append(self.create_spell())

        for _ in range(num_artifacts):
            artifact.append(self.create_artifact())

        return {
            'creatures': creature,
            'spells': spell,
            'artifacts': artifact
        }

    def get_supported_types(self) -> dict:
        """Return supported archetypes for each card category."""
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
