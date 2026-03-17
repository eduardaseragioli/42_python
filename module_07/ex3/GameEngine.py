from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
import random


class GameEngine():

    def __init__(self) -> None:
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.turns_simulated: int = 0
        self.game_stats: dict = {}

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turns_simulated = 0
        self.game_stats = {
            'total_damage': 0,
            'cards_played': 0
        }

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise ValueError("GameEngine is not configured")
        deck = self.factory.create_themed_deck(size=10)
        hand = random.sample(deck['creatures'] +
                             deck['spells'] + deck['artifacts'], 3)

        battlefield: list = []
        result_turn = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.game_stats['total_damage'] += result_turn[
            'actions']['damage_dealt']
        self.game_stats['cards_played'] += len(
            result_turn['actions']['cards_played'])

        return {
            'hand': hand,
            'turn_result': result_turn
        }

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'game_stats': self.game_stats
        }
