import sys


def inventory_system() -> None:
    """
    Analyze and manage inventory from command-line arguments"""
    args: list[str] = sys.argv[1:]
    dictionary: dict[str, int] = {}

    print("=== Inventory System Analysis ===")

    for arg in args:
        try:
            name: str
            quantity: str
            name, quantity = arg.split(":")
            dictionary[name] = int(quantity)
        except ValueError:
            print(f"Error: '{arg}' is not in the correct"
                  + "format (expected item:quantity)")
            print("Usage: python3 ft_inventory_system.py"
                  + "sword:10 potion:5 shield:3")
            return

    if len(dictionary) == 0:
        print("No valid items provided")
        return

    total_units: int = sum(dictionary.values())
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item type: {len(args)}")

    print("\n=== Current Inventory ===")
    sorted_dict: dict[str, int] = dict(
        sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    for item, quantity in sorted_dict.items():
        percentage: float = (quantity / total_units) * 100
        if quantity == 1:
            print(f"{item}: {quantity} unit ({percentage:.1f})")
        else:
            print(f"{item}: {quantity} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most_abundant: str = max(dictionary, key=dictionary.get)
    min_abundant: str = min(dictionary, key=dictionary.get)

    most_quantity: int = dictionary[most_abundant]
    min_quantity: int = dictionary[min_abundant]
    print(f"Most abundant: {most_abundant} ({most_quantity} units)")
    print(f"Least abundant: {min_abundant} ({min_quantity} unit)")

    print("\n=== Item Categories ===")
    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for item, quantity in sorted_dict.items():
        if quantity >= 5:
            categories["Moderate"].update({item: quantity})
        else:
            categories["Scarce"].update({item: quantity})

    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")

    print("\n=== Management Suggestions ===")

    restock: list[str] = [item for item, quantity in sorted_dict.items()
                          if quantity <= 1]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")

    print(f"Dictionary keys: {list(dictionary.keys())}")
    print(f"Dictionary values: {list(dictionary.values())}")


if __name__ == "__main__":
    inventory_system()
