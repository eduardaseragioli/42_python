from ex4.TournamentCard import TournamentCard
import random

class TournamentPlatform():

    def __init__(self):
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("Card is not a TournamentCard")

        card_id = "card_" + str(len(self.cards) + 1)
        self.cards[card_id] = card
        return card_id
    
    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("Card id isn't in the plataform")
        
        if card1_id == card2_id:
            raise ValueError("A card cannot play against itself")
        
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = random.choice([card1, card2])
        loser = card2 if winner is card1 else card1

        winner.update_wins(1)
        loser.update_losses(1)

        winner_rating = winner.calculate_rating()
        loser_rating = loser.calculate_rating()

        self.matches_played += 1

        return {
            'match_number': self.matches_played,
            'card1': card1.name,
            'card2': card2.name,
            'winner': winner.name,
            'loser': loser.name,
            'winner_rating': winner_rating,
            'loser_rating': loser_rating
        }

    def get_leaderboard(self) -> list:
        cards_list = list(self.cards.values())

        for card in cards_list:
            card.calculate_rating()

        sorted_cards = sorted(cards_list, key=lambda c: c.rating, reverse=True)

        leaderboard: list = []
        position = 1

        for card in sorted_cards:
            leaderboard.append({
                'position': position,
                'name': card.name,
                'rating': card.rating,
                'wins': card.wins,
                'losses': card.losses
            })
            position += 1

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        leaderboard = self.get_leaderboard()

        if not leaderboard:
            leader = None
        else:
            leader = leaderboard[0]

        if total_cards == 0:
            avg_rating = 0
        else:
            avg_rating = sum(card.rating for card in self.cards.values()) / total_cards


        return {
            'total_cards': total_cards,
            'total_matches': self.matches_played,
            'leaderboard': leaderboard,
            'leader': leader,
            'avg_rating': avg_rating
        }



