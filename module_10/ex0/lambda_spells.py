def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorter_artifact = sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorter_artifact

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filter_power = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filter_power
    
def spell_transformer(spells: list[str]) -> list[str]:
    transformer_spell = list(map(lambda spell: "* " + spell + " *", spells))
    return transformer_spell

def mage_stats(mages: list[dict]) -> dict:
    max_power =  max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    average_power = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)

    dict_result = {'max_power': max_power["power"], 'min_power': min_power["power"], 'avg_power': average_power}
    return dict_result

def main() -> None:
    print("Testing artifact sorter...")

if __name__ == "__main__":
    main()