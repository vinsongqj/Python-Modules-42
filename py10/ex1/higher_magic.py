from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def combined(target: str, power: int) -> str:
        try:
            res1 = spell1(target, power).replace(f" hits {target} "
                                                 f"for {power} damage",
                                                 f" hits {target}")
            res2 = spell2(target, power).replace(f" restores {target} "
                                                 f"for {power} HP",
                                                 f"s {target}")
            return f"{res1}, {res2}"
        except (TypeError, ValueError, AttributeError):
            return "Error: Spell combination failed"
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        try:
            return base_spell(target, power * multiplier)
        except (TypeError, ValueError, AttributeError):
            return "Error: Amplification failed"
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def cast(target: str, power: int) -> str:
        try:
            if condition(target, power):
                return spell(target, power)
            return "Spell fizzled"
        except (TypeError, ValueError, AttributeError):
            return "Error: Condition check failed"
    return cast


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        try:
            return [s(target, power) for s in spells]
        except (TypeError, ValueError, AttributeError):
            return ["Error: Sequence interrupted"]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 50)}")

    print("\nTesting power amplifier...")
    p = 10
    m = 3
    mega_fireball = power_amplifier(fireball, m)
    print(f"Original: {p}, Amplified: {p * m}")
