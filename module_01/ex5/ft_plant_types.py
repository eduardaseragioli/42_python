class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    
class Flower(Plant):

    def __init__(self, color: str, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self) -> str:
        print (f"{self.name} is blooming beautifully!")
    def get_inf_flower(self):
        print (f"\n{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

class Tree(Plant):

    def __init__(self, trunk_diameter: int, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = 78
        print(
            f"{self.name} provides " 
            f"{shade}" 
            " square meters of shade"
            )
    
    def get_inf_tree(self):
        print(f"\n{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

class Vegetable(Plant):

    def __init__(
        self,
        harvest_season: str,
        nutritional_value: str,
        height: int,
        age: int,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_int(self):
        print(f"{self.name} is rich in {self.nutritional_value} ")
    
    def get_inf_veg(self):
        print(f"\n{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")

if __name__ == "__main__":
    rose = Flower("red", "Rose", 25, 30)
    rose.get_inf_flower()
    rose.bloom()

    daisy = Flower("yellow", "Daisy",20, 45)
    daisy.get_inf_flower()
    daisy.bloom()

    oak = Tree(50, "Oak", 500, 1825)
    oak.get_inf_tree()
    oak.produce_shade()

    cactus = Tree(60, "cactus", 600, 1830)
    cactus.get_inf_tree()
    cactus.produce_shade()

    tomato = Vegetable("summer", "vitamin C", "Tomato", 80, 90)
    tomato.get_inf_veg()
    tomato.nutri_int()

    potato = Vegetable("winter", "vitamin B", "Potato", 70, 80)
    potato.get_inf_veg()
    potato.nutri_int()