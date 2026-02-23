import sys


def test() -> None:
    """
    Display command-line arguments information.

    Prints the program name, number of arguments received,
    each argument with its position, and the total count of arguments.
    """
    print("=== Command Quest ===")

    args = sys.argv
    program_name = args[0].replace("_", "\\_")

    if len(args) < 2:
        print("No arguments provided!")
    print(f"Program name: {program_name}")

    if len(args) > 1:
        print(f"Arguments received: {len(args) - 1}")
    for i, arg in enumerate(args[1:], start=1):
        print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    test()
