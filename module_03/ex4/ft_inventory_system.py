import sys

args = sys.argv[1:]
dictionary = {}

print("=== Inventory System Analysis ===")

try:
    for arg in args:
        name, quantity = arg.split(":")
        dictionary[name] = int(quantity)
except ValueError:
    print("Error: output invalid")

total_units = sum(dictionary.values())
print(f"Total items in inventory: {total_units}")
print(f"Unique item type: {len(args)}")

print("\n=== Current Inventory ===")
sorted_dict = dict(
    sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
for item, quantity in sorted_dict.items():
    percentage = (quantity / total_units) * 100
    if quantity == 1:
        print(f"{item}: {quantity} unit ({percentage:.1f})")
    else:
        print(f"{item}: {quantity} units ({percentage:.1f}%)")

print("\n=== Inventory Statistics ===")

most_abundant = max(dictionary, key=dictionary.get)
min_abundant = min(dictionary, key=dictionary.get)

most_quantity = dictionary[most_abundant]
min_quantity = dictionary[min_abundant]
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

restock = [item for item, quantity in sorted_dict.items() if quantity <= 1]
print(f"Restock needed: {restock}")

print("\n=== Dictionary Properties Demo ===")

print(f"Dictionary keys: {list(dictionary.keys())}")
print(f"Dictionary values: {list(dictionary.values())}")


