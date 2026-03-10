from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Brew healing potion using fire and water elements"""
    fire: str = create_fire()
    water: str = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion() -> str:
    """Brew strength potion using earth and fire elements"""
    earth: str = create_earth()
    fire: str = create_fire()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion() -> str:
    """Brew invisibility potion using air and water elements"""
    air: str = create_air()
    water: str = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    """Brew wisdom potion using all four elements"""
    fire: str = create_fire()
    water: str = create_water()
    earth: str = create_earth()
    air: str = create_air()

    return (
        f"Wisdom potion brewed with all elements: {fire},"
        + f"{water}, {earth}, {air}"
    )
