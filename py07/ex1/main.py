#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    deck = Deck()

    try:
        deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
        deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 3,
                                   "Permanent: +1 mana"))
        deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))

        print("Building deck with different card types...")
        print(f"Deck stats: {deck.get_deck_stats()}")

        print("\nDrawing and playing cards:")
        deck.shuffle()

        for _ in range(3):
            card = deck.draw_card()
            result = card.play({"mana": 10})
            print(f"\nDrew: {card.name} ({card.card_type})")
            print(f"Play result: {result}")

        print("\nPolymorphism in action: Same interface, "
              "different card behaviors!")

    except ValueError as e:
        print(f"Caught expected validation error: {e}")
    except IndexError as e:
        print(f"Caught expected deck error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
