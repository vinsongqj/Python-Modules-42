#!/usr/bin/env python3

from typing import Dict, Any


class Combatable:
    def __init__(self, attack: int, health: int):
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a non-negative integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack_val = attack
        self.health = health

    def attack(self, target: str) -> Dict[str, Any]:
        if not target:
            raise ValueError("Target name cannot be empty")
        return {
            'attacker': getattr(self, 'name', 'Unknown'),
            'target': target,
            'damage': self.attack_val,
            'combat_type': 'melee'
        }

    def defend(self, damage: int) -> Dict[str, Any]:
        if damage < 0:
            raise ValueError("Damage received cannot be negative")

        blocked = 3
        taken = max(0, damage - blocked)
        self.health -= taken
        return {
            'defender': getattr(self, 'name', 'Unknown'),
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': self.health > 0
        }
