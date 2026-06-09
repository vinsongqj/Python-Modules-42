#!/usr/bin/env python3

from ex0.Card import Card
from typing import Dict, Any


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        if not effect_type:
            raise ValueError("Effect type is required")

        self.effect_type = effect_type
        self.card_type = "Spell"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Deal 3 damage to target"
        }

    def resolve_effect(self, targets: list) -> dict:
        return {"effect": self.effect_type, "targets": targets,
                "resolved": True}
