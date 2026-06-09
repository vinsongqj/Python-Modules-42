#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")

    try:
        dragon = CreatureCard(
                                name="FireDragon",
                                cost=5,
                                rarity="Legendary",
                                attack=7,
                                health=5
                             )
        print("\nCreatureCard Info:")
        print(dragon.get_card_info() | {
            "type": "Creature",
            "attack": dragon.attack,
            "health": dragon.health
        })
        available_mana = 6
        print(f"\nPlaying: Fire Dragon with {available_mana} mana available:")
        print(f"Playable: {dragon.is_playable(available_mana)}")

        game_state = {"mana": available_mana}
        print(f"Play result: {dragon.play(game_state)}")

        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

        low_mana = 3
        print(f"\nTesting insufficient mana ({low_mana} available):")
        print(f"Playable: {dragon.is_playable(low_mana)}")

        print("\nAbstract pattern successfully demonstrated!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
