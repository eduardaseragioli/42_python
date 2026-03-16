from ex3 import GameEngine, FantasyCardFactory, AggressiveStrategy

def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    game = GameEngine()
    fantasy = FantasyCardFactory()
    aggressive = AggressiveStrategy()

    print(f"Factory: {fantasy.__class__.__name__}")
    print(f"Strategy: {aggressive.__class__.__name__}")
    print(f"Available types: {fantasy.get_supported_types()}")

    game.configure_engine(fantasy, aggressive)

    print("\nSimulating aggressive turn...")
    turn_data = game.simulate_turn()
    hand = turn_data['hand']
    turn_result = turn_data['turn_result']

    print(f"Hand: {[f'{card.name} ({card.cost})' for card in hand]}")

    print("\nTurn execution:")
 
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions:{turn_result['actions']}")
  
    print("\nGame Report:")
    print(game.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()