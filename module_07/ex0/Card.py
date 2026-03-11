from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> None:
        pass

    def get_card_info(self) -> dict:
        card_info: dict = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': type(self).__name__
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        available_mana = available_mana

        if available_mana >= self.cost:
            return True
        return False
