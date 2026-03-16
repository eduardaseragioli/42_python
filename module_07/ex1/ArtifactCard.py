from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.card_type = 'artifact'

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Permanent: ' + self.effect
        }

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1

            return {
                'artifact': self.name,
                'ability': self.effect,
                'durability_remaining': self.durability,
                'status': 'active'
            }

        else:
            return {
                'artifact': self.name,
                'ability': self.effect,
                'durability_remaining': 0,
                'status': 'destroyed'
            }
        
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = self.card_type  
        return info
