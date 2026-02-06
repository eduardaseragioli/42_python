class Plant:
    """Represents a basic plant with name and height attributes."""
    def __init__(self, name:str, height:int):
        self.name = name
        self.height = height
    
    def grow(self):
        """plant height add by 1 centimeter and print the growth message."""
        self.height += 1
        print (f"{self.name} grew 1cm")

    def base_info(self) -> str:
        """Return basic plant information as a formatted string."""
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    """Represents a flowering plant that extends Plant with color and bloom status."""
    def __init__(self, name:str, height:int, color:str, is_blooming:bool):
        """Initialize a flowering plant with color and blooming state."""
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming
    
    def bloom(self):
        """Set the plant's blooming status to True and print a message."""
        self.is_blooming = True
        print (f" {self.name} is blooming beautifully")
    
    def base_info(self) -> str:
        """Return flowering plant information including flower color and bloom status. """
        if self.is_blooming:
            return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"
        else:
            return f"{self.name}: {self.height}cm, {self.color} flowers"

class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flowering plant with point value."""
    def __init__(self, name:str, height:int, color:str, is_blooming: bool, points:int):
        """Initialize a prize flower with points for competitions. """
        super().__init__(name, height, color, is_blooming)
        self.points = points
    
    def base_info(self) -> str:
        """Return prize flower information including points value."""
        return f"{super().base_info()}, Prize points: {self.points}"

class GardenManager:
    """Manages multiple gardens and their plant collections with analytics."""
    total_gardens_created = 0

    def __init__(self):
        """Initialize a new garden manager with empty gardens and statistics."""
        self.gardens = {}
        self.stats = {}

    @classmethod
    def create_garden_network(cls):
        """Create a pre-configured garden network with Alice and Bob's gardens."""
        maneger = cls()

        maneger.add_garden("Alice")

        oak = Plant("Oak Tree", 100)
        maneger.add_plant("Alice", oak)
        print(f"\nAdded Oak Tree to Alice's garden")

        rose = FloweringPlant("Rose", 25, "red", True)
        maneger.add_plant("Alice", rose)
        print(f"Added Rose to Alice's garden")

        sun = PrizeFlower("Sunflower", 50, "yellow", True, 10)
        maneger.add_plant("Alice", sun)
        print(f"Added Sunflower to Alice's garden")

        maneger.add_garden("Bob")

        pine = Plant("Pine Tree", 50)
        maneger.add_plant("Bob", pine)

        tulip = FloweringPlant("Tulip", 30, "purple", True)
        maneger.add_plant("Bob", tulip)

        lily = PrizeFlower("Lily", 12, "white", True, 0)
        maneger.add_plant("Bob", lily)

        return maneger
    
    @staticmethod
    def format_height(height_cm: int) -> str:
        """Format a height value with centimeter unit.
        Args:
            height_cm: Height value in centimeters. 
        Returns:
            A formatted string with centimeter unit.
        """
        return f"{height_cm}cm"

    def add_garden(self, garden_name: str):
        """Add a new garden to the manager."""
        self.gardens[garden_name] = []
        self.stats[garden_name] = self.GardenStats()
        GardenManager.total_gardens_created += 1
        
    def add_plant(self, garden_name: str, plant: str):
        """Add a plant to a specific garden."""
        self.gardens[garden_name].append(plant)
        self.stats[garden_name].add_plant(plant)

    def do_grow(self, garden_name: str):
        """Grow all plants in a garden by 1 centimeter."""
        for plant in self.gardens[garden_name]:
            plant.grow()
            self.stats[garden_name].record_growth(1)

    def make_report(self, garden_name: str):
        """Generate and print a detailed report for a garden."""
        print(f"\n=== {garden_name}'s Garden Report ===")
        print ("Plants in garden: ")
        for plant in self.gardens[garden_name]:
            print(f"- {plant.base_info()}")
        self.stats[garden_name].generate_report()

    def calculate_score(self, garden_name: str):
        """Calculate the total score for a garden based on plant heights and points.
            The total score combining plant, heights and prize points.
        """
        score = 0
        for plant in self.gardens[garden_name]:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score

    def validate_height(self, garden_name: str, min_height: int):
        """Validate if all plants in a garden meet minimum height requirement.
           True if all plants meet the minimum height, False otherwise.
        """
        for plant in self.gardens[garden_name]:
            if plant.height < min_height:
                return False
        return True

    class GardenStats:
        """Nested helper class that looks statistics for a garden."""

        def __init__(self):
            """Initialize garden statistics with zero values."""
            self.plants_added = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0

        def add_plant(self, plant):
            """Record a new plant and categorize it by type."""
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_count += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_count += 1
            elif isinstance(plant, Plant):
                self.regular_count += 1

        def record_growth(self, amount):
            """Record total growth amount for the garden."""
            self.total_growth += amount

        def generate_report(self):
            """Print the garden statistics report."""
            print(f"\nPlants added: {self.plants_added}, Total growth: {self.total_growth}cm")
            print(f"Plant types: {self.regular_count} regular, {self.flowering_count} flowering, {self.prize_count} prize flowers")

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    manager = GardenManager.create_garden_network()
    print("\nAlice is helping all plants grow...")
    manager.do_grow("Alice")
    manager.make_report("Alice")

    print(f"\nHeight validation test: {manager.validate_height('Alice', 10)}")
    print(f"Garden scores - Alice: {manager.calculate_score('Alice')}, Bob: {manager.calculate_score('Bob')}")
    print(f"Total gardens managed: {GardenManager.total_gardens_created}")


