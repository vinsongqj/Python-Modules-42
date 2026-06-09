#!usr/bin/env python3

from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:

    try:
        engine = GameEngine()
        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()

        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        engine.configure_engine(factory, strategy)

        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        result = engine.simulate_turn()

        print(f"Hand: {result['hand_str']}")
        print("\nTurn execution:")
        print(f"Strategy: {result['execution']['strategy']}")
        print(f"Actions: {result['execution']['actions']}")

        print("\nGame Report:")
        print(engine.get_engine_status())
        print("\nAbstract Factory + Strategy Pattern: Maximum "
              "flexibility achieved!")

    except ValueError as e:
        print(f"Configuration Error: {e}")
    except RuntimeError as e:
        print(f"Game Logic Error: {e}")
    except Exception as e:
        print(f"An unexpected critical error occurred: {e}")


if __name__ == "__main__":
    main()
