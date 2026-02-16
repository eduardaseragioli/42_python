import sys

args = sys.argv[1:]
dictionary = {}

print(f"=== Inventory System Analysis ===")

for arg in args:
    name, quantity = arg.split(":")
    dictionary[name] = int(quantity)

print(f"Total items in inventory: {sum(dictionary.values())}")
print(f"Unique item type: {len(args)}")

print(f"\n=== Current Inventory ===")
print(f"potion: ")