from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    try:
        return sorted(artifacts, key=lambda x: x['power'], reverse=True)
    except (KeyError, TypeError):
        return []


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    try:
        return list(filter(lambda x: x['power'] >= min_power, mages))
    except (KeyError, TypeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda x: f"* {x} *", spells))
    except TypeError:
        return []


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    try:
        if not mages:
            return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

        powers = list(map(lambda x: x['power'], mages))
        return {
            'max_power': int(max(powers)),
            'min_power': int(min(powers)),
            'avg_power': round(sum(powers) / len(powers), 2)
        }
    except (KeyError, TypeError, ZeroDivisionError):
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'Staff'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Orb'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    if sorted_artifacts:
        print("\nTesting artifact sorter...")
        print(f"{sorted_artifacts[0]['name']} "
              f"({sorted_artifacts[0]['power']} power) "
              f"comes before {sorted_artifacts[1]['name']} "
              f"({sorted_artifacts[1]['power']} power)")

    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print("\nTesting spell transformer...")
    print(" ".join(transformed))
