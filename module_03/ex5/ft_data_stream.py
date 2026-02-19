from typing import Generator


def generator_event(count_event: int) -> Generator[tuple[int, str, int, str], None, None]:
    player = ['alice', 'bob', 'charlie', 'ana']
    event = ['killed monster', 'found treasure', 'leveled up']

    for i in range(1, count_event+1):
        player_name = player[i % len(player)]
        action = event[i % len(event)]
        level = (i * 7) % 25

        yield (i, player_name, level, action)


def fibonacc_generator(n: int) -> Generator:
    a = 0
    b = 1
    count = 0

    while count < n:
        yield a

        a, b = b, a + b
        count += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    print("\nProcessing 1000 game events...\n")
    for event_id, player_name, level, action in generator_event(1000):
        if event_id <= 3:
            print(
                f"Event {event_id}:  Player {player_name} (level {level}) {action}")
        if event_id == 4:
            print(" ... ")

    print("\n=== Stream Analytics ===")

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    for event_id, player_name, level, action in generator_event(1000):
        total += 1

        if level >= 10:
            high_level += 1
        if 'treasure' in action:
            treasure += 1
        if 'level-up' in action:
            level_up += 1

    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Leveled up events: {level_up}")

    print("\n=== Generator Demonstration ===")
    fib = fibonacc_generator(10)
    fib_str = ", ".join(str(n) for n in fib)
    print(f"Fibonacci sequence (first 10): {fib_str}")


if __name__ == "__main__":
    main()

"""
def blah(start, end):
    i = start

    while i < end:
        yield i
        i += 1

for n in blah(0, 10):
    print(n)
"""
