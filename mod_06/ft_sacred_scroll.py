import alchemy
import alchemy.elements


def main() -> None:
    """Demonstrate package-level vs module-level access."""
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")

    fire: str = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire}")

    water: str = alchemy.elements.create_water()
    print(f"alchemy.elements.create_water(): {water}")

    earth: str = alchemy.elements.create_earth()
    print(f"alchemy.elements.create_earth(): {earth}")

    air: str = alchemy.elements.create_air()
    print(f"alchemy.elements.create_air(): {air}")

    print("\nTesting package-level access (controlled by __init__.py):")
    result = alchemy.create_fire()
    print(f"alchemy.create_fire(): {result}")

    result = alchemy.create_water()
    print(f"alchemy.create_water(): {result}")

    try:
        result = alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        result = alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    version = alchemy.__version__
    print(f"Version: {version}")

    author = alchemy.__author__
    print(f"Author: {author}")


if __name__ == "__main__":
    main()
