#!/usr/bin/env python3

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost cannot be negative")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Dict[str, Any]:
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity
               }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
