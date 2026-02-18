def water_plants(plant_list):
    """Waters all plants in the list and ensures cleanup happens"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Tests the watering system with normal and error conditions"""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
