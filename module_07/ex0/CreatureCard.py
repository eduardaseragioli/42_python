"""Concrete creature card implementation."""

from ex0.Card import Card


class CreatureCard(Card):
    """Card that can be summoned and attack targets."""

    def __init__(self,  name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        """Create a creature card with combat attributes."""
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer.")

        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")

        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.card_type = 'creature'

    def get_card_info(self) -> dict:
        """Return card metadata including creature stats."""
        info = super().get_card_info()
        info['type'] = self.card_type
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def play(self, game_state: dict) -> dict:
        """Summon creature to battlefield."""
        if not isinstance(game_state, dict):
            raise ValueError("game_state is not a dictionary!")

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        """Deal damage to a target dictionary with health."""
        if 'health' not in target:
            raise ValueError("Target must have a 'health' attribute.")

        target['health'] -= self.attack

        return {
            'attacker': self.name,
            'target': target.get('name', 'Unknown'),
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
