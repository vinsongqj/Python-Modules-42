#!/usr/bin/env python3

from typing import Dict, Any, List


class Magical:
    def __init__(self, mana: int):
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("Initial mana cannot be negative")

        self.mana_power = mana

    def cast_spell(self, spell: str, targets: List[str]) -> Dict[str, Any]:
        if not spell:
            raise ValueError("Spell name required")

        return {
            'caster': 'Arcane Warrior',
            'spell': spell,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        if amount < 0:
            raise ValueError("Cannot channel negative mana")

        self.mana_power += amount
        return {
            'channeled': amount,
            'total_mana': self.mana_power
        }
