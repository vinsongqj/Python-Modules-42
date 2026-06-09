#!/usr/bin/env python3

from ex2.EliteCard import EliteCard


def main() -> None:

    hero = EliteCard("Arcane Warrior", 5, "Rare", 5, 10, 4)

    print("\n=== DataDeck Ability System ===\n")
    try:
        print("EliteCard capabilities:")
        for category, methods in hero.capabilities.items():
            print(f"- {category}: {methods}")

        print(f"\n{hero.play({})}")

        print("\nCombat phase:")
        print(f"Attack result: {hero.attack('Enemy')}")
        print(f"Defense result: {hero.defend(5)}")

        print("\nMagic phase:")
        print(f"Spell cast: {hero.cast_spell('Fireball',
                                             ['Enemy1', 'Enemy2'])}")

        print(f"Mana channel: {hero.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")
    except ValueError as e:
        print(f"Validation Error: {e}")
    except AttributeError as e:
        print(f"Interface Error: Missing expected attribute - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
