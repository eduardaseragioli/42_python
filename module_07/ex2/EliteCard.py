from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 health: int, mana: int, spell_power: int):

        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana = mana
        self.spell_power = spell_power

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("The game_state is not a Dictionary")
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect':
            'combat_power': self.attack_power,
            'magic_power': self.spell_power
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.spell_power = 4

        if self.mana < self.spell_power:
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': self.targets,
                'mana_used': 0,
                'error': 'Not enough mana'
            }
        self.mana -= self.spell_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.spell_cost
        }

    def channel_mana(self, amount: int) -> dict:
        if amount <= 0:
            return {
                'channeled': 0,
                'total_mana': self.mana
                'erro': 'Invalid mana'
            }
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana;
            'spell_power': self.spell_power
        }

    def attack(self, target) -> dict:
        if isinstance(target, dict):
            target_name = target.get('name', 'Enemy')
        else:
            target_name = str(target)
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
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
        return {
            'attack_power': self.attack_power,
            'health': self.health
        }
