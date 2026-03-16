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
                'effect': self.effect
            }

    def attack(self, target) -> dict:

    def calculate_rating(self) -> int:

    def get_tournament_stats(self) -> dict: