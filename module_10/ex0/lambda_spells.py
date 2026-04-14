def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorter_artifact = sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorter_artifact


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filter_power = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filter_power


def spell_transformer(spells: list[str]) -> list[str]:
    transformer_spell = list(map(lambda spell: "* " + spell + " *", spells))
    return transformer_spell


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    average_power = round(
        sum(map(lambda x: x["power"], mages)) / len(mages), 2)

    dict_result = {'max_power': max_power["power"],
                   'min_power': min_power["power"], 'avg_power': average_power}
    return dict_result


def main() -> None:

    artifacts: list = [
        {'name': "Ice Wand", 'power': 104, 'type': "focus"},
        {'name': "Earth Shield", 'power': 85, 'type': "relic"},
        {'name': "Shadow Blade", 'power': 118, 'type': "relic"},
        {'name': "Fire Staff", 'power': 72, 'type': "focus"},
    ]

    mages = [
        {'name': 'Sage', 'power': 98, 'element': 'lightning'},
        {'name': 'Casey', 'power': 68, 'element': 'earth'},
        {'name': 'Zara', 'power': 76, 'element': 'shadow'},
        {'name': 'Luna', 'power': 98, 'element': 'fire'},
        {'name': 'Zara', 'power': 56, 'element': 'ice'}
    ]

    spells = ['meteor', 'earthquake', 'tsunami', 'darkness']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']}"
          + f" ({sorted_artifacts[0]['power']} power)"
          + f" comes before {sorted_artifacts[1]['name']}"
          + f" ({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting power filter...")
    filtered = power_filter(mages, 42)
    print(f"{len(filtered)} mages with power >= 42")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']},"
          f" Avg: {stats['avg_power']}")


if __name__ == "__main__":
    main()
