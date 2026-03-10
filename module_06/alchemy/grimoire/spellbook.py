
def record_spell(spell_name: str, ingredients: str) -> str:
    """Record spell after validating ingredients.

    Args:
        spell_name: Name of the spell to record.
        ingredients: Space-separated ingredient names"""
    from .validator import validate_ingredients

    validate_result = validate_ingredients(ingredients)

    if "VALID" in validate_result:
        return f"Spell recorded: {spell_name} ({validate_result})"
    else:
        return f"Spell rejected: {spell_name} ({validate_result})"
