from ex0.Card import Card

class CreatureCard(Card):

    def __init__(self,  name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer.")

        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")
            
    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state is not a dictionary!")

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to battlefield"
        }

    def attack_target(self, target: dict) -> dict:
        if 'health' not in target:
            raise ValueError("Target must have a 'health' attribute.")
        
        target['health'] -= self.attack
        
        return {
            'attacker': self.name,
            'target': target.get('name', 'Unknown'),
            'damage_dealt': self.attack,
            'combat_resolver': target['health'] <= 0
        }

