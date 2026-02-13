class Plant:
    """It represents a plant in the garden with its characteristics.

    Attributes:
        name (str): name of the plant
        height (int): height of the plant in centimeters
        age (int): age of the plant in days
    """

    def __init__(self, name: str, height: int, age: int):

        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """Displays information about multiple plants in the garden.

    Prints each plant's data (name, height, and age) in a formatted format.

    Returns:
    None
    """
    rose = Plant("Rose", 25, 30)
    sun = Plant("Sunflower", 80, 45)
    cac = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sun.name}: {sun.height}cm, {sun.age} days old")
    print(f"{cac.name}: {cac.height}cm, {cac.age} days old")


if __name__ == "__main__":
    ft_garden_data()
