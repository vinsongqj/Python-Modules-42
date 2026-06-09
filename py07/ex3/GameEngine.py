
from typing import Dict, Any, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if not factory or not strategy:
            raise ValueError("Factory and Strategy must be provided")
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine not configured")

        try:
            self.turns += 1
            c1 = self.factory.create_creature("dragon")
            c2 = self.factory.create_creature("goblin")
            c3 = self.factory.create_spell()
            self.cards_created += 3

            hand = [c1, c2, c3]
            turn_data = self.strategy.execute_turn(hand, [])
            self.total_damage += turn_data['actions']['damage_dealt']

            return {
                "hand_str": [f"{c.name} ({c.cost})" for c in hand],
                "execution": turn_data
            }
        except Exception as e:
            raise RuntimeError(f"Simulation failed: {e}")

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            'turns_simulated': self.turns,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
