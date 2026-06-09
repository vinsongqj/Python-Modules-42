#!/usr/bin/env python3

from typing import Dict, List, Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registry: Dict[str, TournamentCard] = {}
        self.match_count = 0

    def register_card(self, card: "TournamentCard") -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("Only TournamentCard instances can be registered")
        self.registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        if card1_id not in self.registry or card2_id not in self.registry:
            missing = card1_id if card1_id not in self.registry else card2_id
            raise KeyError(f"Card ID '{missing}' not found in registry")

        winner = self.registry[card1_id]
        loser = self.registry[card2_id]

        winner.update_wins(1)
        loser.update_losses(1)
        self.match_count += 1

        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> List[str]:
        sorted_cards = sorted(self.registry.values(), key=lambda x: x.rating,
                              reverse=True)
        return [f"{c.name} - Rating: {c.rating} ({c.wins}-{c.losses})" for c in
                sorted_cards]

    def generate_tournament_report(self) -> Dict[str, Any]:
        ratings = [c.rating for c in self.registry.values()]
        avg = sum(ratings) // len(ratings) if ratings else 0
        return {
            'total_cards': len(self.registry),
            'matches_played': self.match_count,
            'avg_rating': avg,
            'platform_status': 'active'
        }
