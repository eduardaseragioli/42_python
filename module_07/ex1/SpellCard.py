from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.card_type = 'spell'

    def get_effect_description(self) -> str:
        if self.effect_type == "damage":
            effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            effect = "Heal targets"
        elif self.effect_type == "buff":
            effect = "Buff targets"
        elif self.effect_type == "debuff":
            effect = "Debuff target"
        else:
            effect = "Unknown effect"
        return effect

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.get_effect_description(),
            'consumed': True
        }

    def resolve_effect(self, targets: list) -> dict:

        return {
            'spell_name': self.name,
            'effect_type': self.effect_type,
            'targets_affected': len(targets),
            'result': self.get_effect_description()
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = self.card_type
        return info
