#!/usr/bin/env python3

from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity, attack, health, mana):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health)
        Magical.__init__(self, mana)
        self.card_type = "Elite Card"
        self.capabilities = {
            "Card": ["play", "get_card_info", "is_playable"],
            "Combatable": ["attack", "defend", "get_combat_stats"],
            "Magical": ["cast_spell", "channel_mana", "get_magic_stats"]
        }

    def play(self, game_state: Dict[str, Any]):
        return f"Playing {self.name} ({self.card_type}):"

    def get_card_info(self):
        pass

    def is_playable(self):
        pass
