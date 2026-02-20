import math


def exercise_tuple():
    print("=== Game Coordinate System ===")

    point: tuple[int, int, int] = (10, 20, 5)
    num_inicial: tuple[int, int, int] = (0, 0, 0)

    print(f"\nPosition created: {point}")

    distance = math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)
    print(f"Distance between {num_inicial} and {point}: {distance:.2f}")

    coordinates: str = "3,4,0"
    print(f"\nParsing coordinates: \"{coordinates}\"")

    x, y, z = coordinates.split(",")
    try:
        x: int = int(x)
        y: int = int(y)
        z: int = int(z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    coordinates_split = (x, y, z)
    print(f"Parsed position: {coordinates_split}")

    distance_split = math.sqrt(
        coordinates_split[0]**2 + coordinates_split[1]**2 +
        coordinates_split[2]**2)
    print(
        f"Distance between {num_inicial} and"
        + f"{coordinates_split}: {distance_split}")

    coordinates_str: str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{coordinates_str}\"")

    x, y, z = coordinates_str.split(",")
    try:
        x: int = int(x)
        y: int = int(y)
        z: int = int(z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = coordinates_split
    print(f"Player at x={x}, y={y}, z={z}")
    print(
        f"Coordinates: X={coordinates_split[0]}, Y={coordinates_split[1]},"
        + f"Z={coordinates_split[2]}")


if __name__ == "__main__":
    exercise_tuple()
