def check_temperature(temp_str: str):
    """Validates and checks if the given temperature is suitable for plants."""
    
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    """
    Tests the check_temperature function with various inputs."""

    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    check_temperature("")
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()


