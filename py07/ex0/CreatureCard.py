from ex0.Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a non-negative integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        self.attack = attack
        self.health = health
        self.card_type = "Creature"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: str) -> Dict[str, Any]:
        if not isinstance(target, str) or not target.strip():
            raise ValueError("Target name must be a non-empty string")
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
