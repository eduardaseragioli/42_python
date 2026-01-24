def ft_seed_inventory(seed_type: str, quantity: int, unit: str)->None:
    upper = seed_type.capitalize()
    if unit == "packets":
        print(f"{upper} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{upper} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{upper} seeds: covers {quantity} sqare meters")
    else:
        print("Unknown unit type")

# ft_seed_inventory("tomato", 15, "packets")
# ft_seed_inventory("carrot", 8, "grams")
# ft_seed_inventory("lettuce", 12, "area")
# ft_seed_inventory("grapes ", 7, "grams")
# ft_seed_inventory("grapes ", 7, "kg")
