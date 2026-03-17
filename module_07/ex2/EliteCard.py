"""Elite card implementing both combat and magical interfaces."""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Hybrid card with melee and spellcasting capabilities."""

    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 health: int, mana: int, spell_power: int) -> None:
        """Initialize elite card attributes."""

        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana = mana
        self.spell_power = spell_power

    def play(self, game_state: dict) -> dict:
        """Play elite card and expose combat/magic stats."""
        if not isinstance(game_state, dict):
            raise ValueError("The game_state is not a Dictionary")
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Elite card played successfully",
            'combat_power': self.attack_power,
            'magic_power': self.spell_power
        }

    def cast_spell(self, spell_name: str, targets) -> dict:
        """Cast a spell if enough mana is available."""
        if self.mana < self.spell_power:
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': 0,
                'error': 'Not enough mana'
            }
        self.mana -= self.spell_power
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.spell_power
        }

    def channel_mana(self, amount: int) -> dict:
        """Increase mana pool by a positive amount."""
        if amount <= 0:
            return {
                'channeled': 0,
                'total_mana': self.mana,
                'error': 'Invalid mana'
            }
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        """Return magical attributes."""
        return {
            'mana': self.mana,
            'spell_power': self.spell_power
        }

    def attack(self, target) -> dict:
        """Attack a dictionary target or a generic object."""
        if isinstance(target, dict):
            target_name = target.get('name', 'Enemy')
        else:
            target_name = str(target)
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        """Block part of incoming damage and update health."""
        damage_blocked = min(3, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        still_alive = self.health > 0
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': still_alive
        }

    def get_combat_stats(self) -> dict:
        """Return combat attributes."""
        return {
            'attack_power': self.attack_power,
            'health': self.health
        }
