#!/usr/bin/env python3

def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    a = ['first_blood', 'pixel_perfect', 'speed_runner', 'first_blood',
         'first_blood']
    b = ['first_blood', 'boss_hunter', 'treasure_seeker', 'level_master',
         'level_master']
    c = ['treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood',
         'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood']
    try:
        alice = set(a)
        bob = set(b)
        charlie = set(c)
        print(f"Player alice achievements: {alice}")
        print(f"Player bob achievements: {bob}")
        print(f"Player charlie achievements: {charlie}")
        print("\n=== Achievement Analytics ===")
        achievements = alice.union(bob).union(charlie)
        print(f"All unique achievements: {achievements}")
        print(f"Total unique achievements: {len(achievements)}")
        common = alice.intersection(bob).intersection(charlie)
        print(f"\nCommon to all players: {common}")
        only_alice = alice.difference(bob.union(charlie))
        only_bob = bob.difference(alice.union(charlie))
        only_charlie = charlie.difference(alice.union(bob))
        rare = only_alice.union(only_bob).union(only_charlie)
        print(f"Rare achievements (1 player): {rare}\n")
        alice_vs_bob_common = alice.intersection(bob)
        print(f"Alice vs Bob common: {alice_vs_bob_common}")
        alice_unique = alice.difference(bob)
        print(f"Alice unique: {alice_unique}")
        bob_unique = bob.difference(alice)
        print(f"Bob unique: {bob_unique}")
    except TypeError as e:
        print(f"Error: Achievement list contains invalid data. Details: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ft_achievement_tracker()
