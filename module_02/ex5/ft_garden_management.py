class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 100

    def water_plants(self) -> None:
        try:
            for plant in self.plants:
                if self.water_tank < 5:
                    raise WaterError("Not enough water in tank")
                self.plants[plant]["water"] += 5
                self.water_tank -= 5
                print(f"Watering {plant} -  success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")

    def add_plant(self, plant_name) -> str:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[plant_name] = {"water": 0, "sun": 0}
        return f"Added {plant_name} successfully"

    def check_plant_health(self, plant_name,
                           water_level, sunlight_hours) -> str:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        return f"{plant_name}: healthy (water: {water_level},"
        f"sun: {sunlight_hours})"


def test_garden_management():
    print("=== Garden Management System ===")

    manager = GardenManager()
    print("\nAdding plants to garden...")
    try:
        print(manager.add_plant("tomato"))
        print(manager.add_plant("lettuce"))
        print(manager.add_plant(""))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    print("Opening watering system")

    manager.water_plants()
    print("Closing watering system (cleanup)")

    try:
        manager.check_plant_health("tomato", 5, 8)
    except PlantError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_plant_health("lettuce", 5, 11)

    except (GardenError, PlantError, WaterError) as e:
        print(f"Error: {e}")

    print("\nChecking plant health...")
    try:
        result = manager.check_plant_health("tomato", 5, 8)
        print(result)
    except PlantError as e:
        print(f"Error checking tomato: {e}")
    try:
        manager.check_plant_health("lettuce", 15, 6)
        print
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        manager.water_tank = 2
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
