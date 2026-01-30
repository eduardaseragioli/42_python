class SecurePlant:
    """Represents a secure plant with data validation and encapsulation.
    
    This class protects plant data from corruption by validating all
    modifications through controlled setter methods.
    
    Attributes:
        name (str): The name of the plant
        _height (int): The height of the plant in centimeters (private)
        _age (int): The age of the plant in days (private _ )
    """
    
    def __init__(self, name: str, height: int, age: int):
        """Initializes a secure plant with validated data.
        """
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: int):
        """Sets the plant's height with validation.
        
        Validates that the height is not negative before updating.
        Prints appropriate messages for success or rejection.
        
        Args:
            new_height (int): The new height value in centimeters
            
        Returns:
            bool: True if update successful, False if rejected
        """
        if new_height < 0:
            print(f"\nInvalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def get_height(self) -> int:
        """Gets the plant's current height.
        
        Returns:
            int: The current height in centimeters
        """
        return self._height

    def set_age(self, new_age: int):
        """Sets the plant's age with validation.
        
        Validates that the age is not negative before updating.
        Prints appropriate messages for success or rejection.
        
        Args:
            new_age (int): The new age value in days
            
        Returns:
            bool: True if update successful, False if rejected
        """
        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_age(self) -> int:
        """Gets the plant's current age.
        Returns:
            int: The current age in days
        """
        return self._age
        
    def get_info(self) -> str:
        """Returns formatted information about the plant.
        """
        return f"{self.name} ({self._height}cm, {self._age} days)"
    
def ft_garden_security() -> None:
    """Demonstrates the garden security system with data validation.
    """
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {plant.name}")
          
    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    #plant.set_age(-5)

    print(f"\nCurrent plant: {plant.get_info()}")

if __name__ == "__main__":
    ft_garden_security()