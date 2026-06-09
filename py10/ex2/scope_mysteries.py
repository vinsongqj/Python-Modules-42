from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        try:
            count += 1
            return count
        except (TypeError, ValueError):
            return 0
    return counter


def spell_accumulator(base: int) -> Callable[[int], int]:
    current_total = base

    def accumulator(power: int) -> int:
        nonlocal current_total
        try:
            current_total += power
            return current_total
        except (TypeError, ValueError):
            return current_total
    return accumulator


def enchantment_factory(prefix: str) -> Callable[[str], str]:
    def factory(spell_name: str) -> str:
        try:
            return f"{prefix} {spell_name}"
        except (TypeError, ValueError):
            return spell_name
    return factory


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def setter(key: str, value: Any) -> None:
        try:
            vault[key] = value
        except (TypeError, KeyError):
            pass

    def getter(key: str) -> Any:
        try:
            return vault.get(key, "Memory not found")
        except (TypeError, KeyError):
            return "Memory not found"

    return {"store": setter, "recall": getter}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flaming")
    frost = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frost("Shield"))

    print("\nTesting memory vault...")
    v = memory_vault()
    v["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {v['recall']('secret')}")
    print(f"Recall 'unknown': {v['recall']('unknown')}")
