class Plant:
    """Base class for all plants with common attributes."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with basic attributes.
        Args:
            name: The name of the plant
            height: The height in centimeters
            age: The age in days
        """
        self.name = name
        self.height = height
        self.age = age

    def base_info(self) -> str:
        """Return formatted string with height and age information."""
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    """Flower type plant with color attribute and bloom capability."""

    def __init__(self, color: str, name: str, height: int, age: int):
        """Initialize a flower with color and basic plant attributes."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """Display blooming message for the flower."""
        print(f"{self.name} is blooming beautifully!")

    def get_inf_flower(self):
        """Display complete information about the flower."""
        print(
            f"\n{self.name} (Flower): "
            + f"{self.base_info()}, {self.color} color")


class Tree(Plant):
    """Tree type plant with trunk diameter and shade production."""

    def __init__(self, trunk_diameter: int, name: str, height: int, age: int):
        """Initialize a tree with trunk diameter and basic plant attributes"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Display the amount of shade provided by the tree."""
        shade = (self.trunk_diameter * self.height) // 320
        print(f"{self.name} provides {shade} square meters of shade")

    def get_inf_tree(self):
        """Display complete information about the tree."""
        print(
            f"\n{self.name} (Tree): {self.base_info()}, "
            + f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """Vegetable type plant with harvest season and nutritional value."""

    def __init__(self, harvest_season: str, nutritional_value: str,
                 name: str, height: int, age: int):
        """Initialize vegetable with harvest info and basic plant attributes"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_int(self):
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_inf_veg(self):
        """Display complete information about the vegetable."""
        print(
            f"\n{self.name} (Vegetable): {self.base_info()}, "
            + f"{self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("red", "Rose", 25, 30)
    rose.get_inf_flower()
    rose.bloom()

    daisy = Flower("yellow", "Daisy", 20, 45)
    daisy.get_inf_flower()
    daisy.bloom()

    oak = Tree(50, "Oak", 500, 1825)
    oak.get_inf_tree()
    oak.produce_shade()

    cactus = Tree(60, "Cactus", 600, 1830)
    cactus.get_inf_tree()
    cactus.produce_shade()

    tomato = Vegetable("summer", "Vitamin C", "Tomato", 80, 90)
    tomato.get_inf_veg()
    tomato.nutri_int()

    potato = Vegetable("winter", "Vitamin B", "Potato", 70, 80)
    potato.get_inf_veg()
    potato.nutri_int()
