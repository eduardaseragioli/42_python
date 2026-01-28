class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: int) -> bool:
        if new_height < 0:
            print("Security: Negative height rejected")
            return False
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")
            return True

    def get_height(self) -> int:
        return self._height

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print("Security: Negative age rejected")
            return False
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")
            return True
            
    def get_age(self) -> int:
        return self._age
        
    def get_info(self) -> str:
        return f"{self.name} ({self._height}cm, {self._age} days)"
    
def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 0, 0)
    print(f"Plant created: {plant.name}")
          
    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    print("\nInvalid operation attempted: height -5cm [REJECTED]")

    print(f"\nCurrent plant: {plant.get_info()}")

if __name__ == "__main__":
    ft_garden_security()