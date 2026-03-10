from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmute lead to gold using fire element"""
    fire: str = create_fire()
    return f"Lead transmuted to gold using {fire}"


def stone_to_gem() -> str:
    """Transmute stone to gem using earth element"""
    earth: str = create_earth()
    return f"Stone transmuted to gem using {earth}"
