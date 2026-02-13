class Plant:
    """Represents a plant created by the factory.

    Attributes:
        name (str): The name of the plant
        height (int): The starting height of the plant in centimeters
        age (int): The starting age of the plant in days
    """

    def __init__(self, name: str, starting_height: int, starting_age: int):
        """Initializes a new plant with starting values."""
        self.name = name
        self.height = starting_height
        self.age = starting_age


def ft_plant_factory() -> None:
    """Creates multiple plants efficiently using the factory pattern.

    Initializes at least 5 different plants with varying characteristics
    and displays them in an organized format with the total count.
    """
    factory = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    garden = factory

    print("=== Plant Factory Output ===")

    i = 0
    for plant in garden:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        i += 1

    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
