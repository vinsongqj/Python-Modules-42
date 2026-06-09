
import random
from typing import Dict, Any, List
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int |
                        None = None) -> CreatureCard:
        if name_or_power == "dragon" or name_or_power == 5:
            return CreatureCard("Fire Dragon", 5, "Rare", 5, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 3, 1)

    def create_spell(self, name_or_power: str | int |
                     None = None) -> SpellCard:
        return SpellCard("Lightning Bolt", 3, "Common", "Damage")

    def create_artifact(self, name_or_power: str | int |
                        None = None) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 1, "Uncommon", 5, "Mana Boost")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        if size <= 0:
            raise ValueError("Deck size must be positive")
        deck = []
        for _ in range(size):
            choice = random.choice(['creature', 'spell', 'artifact'])
            if choice == 'creature':
                deck.append(self.create_creature())
            elif choice == 'spell':
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {"theme": "Fantasy", "cards": deck, "size": len(deck)}

    def get_supported_types(self) -> Dict[str, List[str]]:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
