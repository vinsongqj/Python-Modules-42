#!/usr/bin/env python3

import random
from typing import List, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck")
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if not self._cards:
            raise IndexError("Cannot draw from an empty deck")
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict:
        if not self._cards:
            return {"total_cards": 0}

        total_cost = sum(card.cost for card in self._cards)
        total_cards = len(self._cards)
        counts = {"Creature": 0, "Spell": 0, "Artifact": 0}

        for card in self._cards:
            if isinstance(card, CreatureCard):
                counts["Creature"] += 1
            elif isinstance(card, SpellCard):
                counts["Spell"] += 1
            elif isinstance(card, ArtifactCard):
                counts["Artifact"] += 1

        return {
            "total_cards": len(self._cards),
            "creatures": counts["Creature"],
            "spells": counts["Spell"],
            "artifacts": counts["Artifact"],
            "avg_cost": round(total_cost / total_cards, 1)
        }
