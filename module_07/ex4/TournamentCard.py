from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
            self, name: str, cost: int,
            rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
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
            target.health -= self.attack_power
            target_name = target.name if hasattr(target, 'name') else "Unknown"
        else:
            target['health'] -= self.attack_power
            target_name = target.get('name', 'Unknown')

        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack_power,
            'combat_resolved': True
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Error")
        if incoming_damage < 0:
            raise ValueError("Error")

        health_before = self.health

        self.health = self.health - incoming_damage

        if self.health < 0:
            self.health = 0

        defeated = (self.health == 0)

        return {
            'defender': self.name,
            'damage_receiver': incoming_damage,
            'health_before': health_before,
            'health_after': self.health,
            'defeated': defeated
        }

    def get_combat_stats(self) -> dict:
        alive = (self.health > 0)

        return {
            'name': self.name,
            'attack_power': self.attack_power,
            'current_health': self.health,
            'alive': alive
        }

    def calculate_rating(self) -> int:
        base_rating = 1200
        win_points = 25
        loss_points = 15

        new_rating = base_rating + \
            (self.wins * win_points) - (self.losses * loss_points)

        if new_rating < 0:
            new_rating = 0

        self.rating = new_rating
        return new_rating

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("The wins must be a non negative integer")

        self.wins = self.wins + wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("The losses must be a non negative integer")

        self.losses = self.losses + losses

    def get_rank_info(self) -> dict:
        self.calculate_rating()

        record = str(self.wins) + "-" + str(self.losses)

        return {
            'name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses,
            'record': record
        }

    def get_tournament_stats(self) -> dict:
        total_matches = self.wins + self.losses

        if total_matches > 0:
            win_rate = (self.wins / total_matches) * 100
        else:
            win_rate = 0.0

        current_rating = self.calculate_rating()

        return {
            'name': self.name,
            'win': self.wins,
            'losses': self.losses,
            'total_matches': total_matches,
            'win_rate': win_rate,
            'rating': current_rating
        }
