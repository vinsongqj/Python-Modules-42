# AggressiveStrategy.py
import enum
from typing import List, Dict, Any
from ex3.GameStrategy import GameStrategy


class TargetPriority(enum.Enum):
    PLAYER = 1
    CREATURE = 2


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Any]) -> List[str]:
        if not available_targets:
            return ["Enemy Player"]
        return sorted(available_targets, key=lambda x: getattr(x, 'health', 0))

    def execute_turn(self, hand: List[Any],
                     battlefield: List[Any]) -> Dict[str, Any]:
        played_cards = [card for card in hand if card.cost <= 3]
        damage = sum(getattr(c, 'attack', 0) for c in battlefield)

        for card in played_cards:
            if hasattr(card, 'attack'):
                damage += card.attack

            elif card.name == "Lightning Bolt":
                damage += 5

        return {
            'strategy': self.get_strategy_name(),
            'actions': {
                'cards_played': [c.name for c in played_cards],
                'mana_used': sum(c.cost for c in played_cards),
                'targets_attacked': self.prioritize_targets(battlefield),
                'damage_dealt': damage
            }
        }
