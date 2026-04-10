def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorter_artifact = sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorter_artifact

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    
