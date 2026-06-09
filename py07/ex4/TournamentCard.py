#!/usr/bin/env python3

from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id, name, cost, rarity, attack, health,
                 initial_rating=1200):

        if initial_rating < 0:
            raise ValueError("Initial rating cannot be negative")
        if not card_id:
            raise ValueError("Card ID is required")

        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health)

        self.card_id = card_id
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("Wins cannot be negative")
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("Losses cannot be negative")
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> Dict[str, Any]:
        return {"rating": self.rating, "record": f"{self.wins}-{self.losses}"}

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {"action": "Tournament play", "card": self.name}

    def attack(self, target) -> Dict[str, Any]:
        return {"attacker": self.name, "damage": self.attack_val}

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
