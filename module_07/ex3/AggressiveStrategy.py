from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_used = 0
        cards_played: list = []
        targets_attacked: list = [] 
        damage_dealt = 0

        hand.sort(key=lambda card: card.cost)

        for card in hand:
            if mana_used + card.cost <= 5:
                cards_played.append(card.name)
                mana_used += card.cost

                if card.card_type == 'creature':
                    battlefield.append(card)

        for creature in battlefield:
            targets_attacked.append("Enemy Player")
            damage_dealt += creature.attack
        
        return {
            'strategy': self.get_strategy_name(),
            'actions': {
                'cards_played': cards_played,
                'mana_used': mana_used,
                'targets_attacked': targets_attacked,
                'damage_dealt': damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        list_priority: list = sorted(
            available_targets, key=lambda target: target['health']
        )
        return list_priority