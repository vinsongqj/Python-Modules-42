#!/usr/bin/env python3

from ex0.Card import Card
from typing import Dict, Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability < 0:
            raise ValueError("Durability must be a non-negative integer")
        self.durability = durability
        self.effect_description = effect
        self.card_type = "Artifact"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Permanent: +1 mana per turn"
        }

    def activate_ability(self) -> Dict[str, Any]:
        return {"action": self.effect_description,
                "durability_remaining": self.durability}
