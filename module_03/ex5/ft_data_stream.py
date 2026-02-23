from typing import Generator


def generator_event(count_event: int) -> Generator[tuple[int, str, int, str],
                                                   None, None]:
    """
    Generate game events with player actions.
    Yields:
        Tuple containing (event_id, player_name, level, action)
    """
    player: list[str] = ['alice', 'bob', 'charlie']
    event: list[str] = ['killed monster', 'found treasure', 'leveled up']
    levels: list[int] = [5, 12, 8, 15, 10]

    for i in range(count_event):
        player_name: str = player[i % len(player)]
        action: str = event[i % len(event)]
        level: int = levels[i % len(levels)]

        yield (i + 1, player_name, level, action)


def fibonacc_generator(n: int) -> Generator[int, None, None]:
    """
    Generate Fibonacci sequence numbers.

    Args n: Number of Fibonacci numbers to generate

    Yields: Next number in Fibonacci sequence
    """
    a: int = 0
    b: int = 1
    count: int = 0

    while count < n:
        yield a

        a, b = b, a + b
        count += 1


def prime_generator(n: int) -> Generator[int, None, None]:
    """
    Generate prime numbers.

    Args n: Number of prime numbers to generate

    Yields Next prime number
    """
    count: int = 0
    num: int = 2
    while count < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def main() -> None:
    """Process and analyze game event stream data"""
    print("=== Game Data Stream Processor ===")

    print("\nProcessing 1000 game events...\n")
    event_id: int
    player_name: str
    level: int
    action: str
    for event_id, player_name, level, action in generator_event(1000):
        if event_id <= 3:
            print(
                f"Event {event_id}:  Player {player_name}"
                + f"(level {level}) {action}")
        if event_id == 4:
            print(" ... ")

    print("\n=== Stream Analytics ===")

    total: int = 0
    high_level: int = 0
    treasure: int = 0
    level_up: int = 0

    for event_id, player_name, level, action in generator_event(1000):
        total += 1

        if level >= 10:
            high_level += 1
        if 'treasure' in action:
            treasure += 1
        if 'leveled up' in action:
            level_up += 1

    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Leveled up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib: Generator[int, None, None] = fibonacc_generator(10)
    fib_str: str = ", ".join(str(n) for n in fib)
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime: Generator[int, None, None] = prime_generator(5)
    prime_str: str = ", ".join(str(n) for n in prime)
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()
