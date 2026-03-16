from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("Game state is not a dictionary")

        if 'mana' in game_state:
            game_state['mana'] -= self.cost
        else:
            game_state['mana'] = 0

        if hasattr(self, 'card_type'):
            if self.card_type == 'creature':
                effect = "Creature summoned to battlefield"
            elif self.card_type == 'spell':
                effect = "Spell cast"
            elif self.card_type == 'artifact':
                effect = "Artifact activated"
            else:
                effect = "Unknown effect"
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': effect
            }

    def attack(self, target) -> dict:
        if not hasattr(target, 'health') and 'health' not in target:
            raise ValueError("The target dosent't have health")

        if hasattr(target, 'health'):
            target.health -= self.attack
            target_name = target.name if hasattr(target, 'name') else "Unknown"
        else:
            target['health'] -= self.attack
            target_name = target.get('name', 'Unknown')

        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }


    def calculate_rating(self) -> int:

    def get_tournament_stats(self) -> dict: