def garden_intro() -> None:

    """
        Displays information about a plant in the garden.

        Prints the plant's data (name, height, and age) in a formatted format with welcome and closing headers.

        Returns:
        None
    """
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")

if __name__ == "__main__":
    garden_intro()
