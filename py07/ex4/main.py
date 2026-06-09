from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    try:
        platform = TournamentPlatform()

        c1 = TournamentCard("dragon_001", "Fire Dragon", 5, "Rare", 5, 5, 1200)
        c2 = TournamentCard("wizard_001", "Ice Wizard", 4, "Rare", 3, 4, 1150)

        platform.register_card(c1)
        platform.register_card(c2)

        print("\n=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...\n")

        for c in [c1, c2]:
            print(f"{c.name} (ID: {c.card_id}):")
            print("- Interfaces: [Card, Combatable, Rankable]")
            print(f"- Rating: {c.rating}")
            print(f"- Record: {c.wins}-{c.losses}\n")

        print("Creating tournament match...")
        match_result = platform.create_match("dragon_001", "wizard_001")
        print(f"Match result: {match_result}")

        print("\nTournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        for i, entry in enumerate(leaderboard, 1):
            print(f"{i}. {entry}")

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except ValueError as e:
        print(f"Validation Error: {e}")
    except KeyError as e:
        print(f"Registry Error: {e}")
    except Exception as e:
        print(f"Critical System Failure: {e}")


if __name__ == "__main__":
    main()
