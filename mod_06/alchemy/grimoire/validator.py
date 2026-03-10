def validate_ingredients(ingredients: str) -> str:
    """Validate spell ingredients.

    Args:
        ingredients: Space-separated ingredient names"""
    if not isinstance(ingredients, str):
        return f"{ingredients} - INVALID"
    elements: list[str] = ["fire", "water", "earth", "air"]
    each_ingredients = ingredients.split()
    for ingredient in each_ingredients:
        if ingredient not in elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
