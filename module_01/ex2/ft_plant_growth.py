class Plant:
    """Represents a plant in the garden with growth capabilities.
    
    Attributes:
        name (str): The name of the plant
        height (int): The height of the plant in centimeters
        age (int): The age of the plant in days
        initial_height (int): The initial height used to track growth
    """
    
    def __init__(self, name: str, height: int, age: int):
        """Initializes a new plant.
        """
        self.name = name.capitalize()
        self.height = height
        self.age_day = age
        self.initial_height = height

    def grow(self):
        """Increases the plant's height by 1 centimeter."""
        self.height += 1

    def age(self):
        """Increases the plant's age by 1 day."""
        self.age_day += 1

    def get_info(self) -> str:
        """Returns formatted information about the plant.
        
        Returns:
            A string containing the plant's name, height, and age
        """
        return f"{self.name}: {self.height}cm, {self.age_day} days old"
    
def ft_plant_growth() -> None:
    """Simulates plant growth over a week.
    
    Creates multiple plants and displays their information at day 1 and day 7,
    showing how they grow over time with increments in height and age.

    """
    rose = Plant("rose", 25, 30)
    sun = Plant("Sunflower", 80, 45)
    cac = Plant("Cactus", 15, 120)

    print("=== Day 1 ===")
    print(rose.get_info())
    print(sun.get_info())
    print(cac.get_info())

    for day in range(6):
        rose.grow()
        rose.age()
        sun.grow()
        sun.age()
        cac.grow()
        cac.age()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(sun.get_info())
    print(cac.get_info())

    print(f"Growth this week: +{rose.height - rose.initial_height}cm\n")

if __name__ == "__main__":
    ft_plant_growth()