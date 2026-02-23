def achivement() -> None:
    """
    Track and analyze player achievements using sets.

    Demonstrates set operations including union, intersection, and
    difference to find unique achievements, common achievements across
    players, rare achievements held by only one player, and
    player-specific comparisons.
    """
    print("=== Achievement Tracker System ===")

    alice: set[str] = {'first_kill', 'level_10',
                       'treasure_hunter', 'speed_demon'}
    bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set[str] = {'level_10', 'treasure_hunter',
                         'boss_slayer', 'speed_demon', 'perfectionist'}

    print(f"\nPlayer alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_achivement: set[str] = alice.union(bob, charlie)
    len_all_achivement: int = len(all_achivement)
    print(f"All unique achievements: {all_achivement}")
    print(f"Total unique achievements: {len_all_achivement}")

    common_achivement: set[str] = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common_achivement}")

    alice_unique: set[str] = alice - bob - charlie
    bob_unique: set[str] = bob - charlie - alice
    charlie_unique: set[str] = charlie - alice - bob

    rare_achivement: set[str] = alice_unique | bob_unique | charlie_unique
    print(f"Rare achievements (1 player): {rare_achivement}")

    alice_bob: set[str] = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {alice_bob}")

    alice_unique_bob: set[str] = alice - bob
    print(f"Alice unique: {alice_unique_bob}")

    bob_unique_alice: set[str] = bob.difference(alice)
    print(f"Bob unique: {bob_unique_alice}")


if __name__ == "__main__":
    achivement()
