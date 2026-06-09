import functools
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    try:
        if not spells:
            return 0

        if operation in ("sum", "add"):
            return functools.reduce(operator.add, spells)
        if operation in ("product", "multiply"):
            return functools.reduce(operator.mul, spells)
        if operation == "max":
            return functools.reduce(lambda a, b: a if a > b else b, spells)
        if operation == "min":
            return functools.reduce(lambda a, b: a if a < b else b, spells)

        return 0
    except (TypeError, ValueError):
        return 0


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    try:
        return {
            "fire": functools.partial(base_enchantment, 50, "fire"),
            "ice": functools.partial(base_enchantment, 50, "ice"),
            "thunder": functools.partial(base_enchantment, 50, "thunder")
        }
    except (TypeError, AttributeError):
        return {}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    try:
        if n < 0:
            return 0
        if n <= 1:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    except (TypeError, RecursionError):
        return 0


@functools.singledispatch
def spell_dispatcher(spell: Any) -> str:
    return "Unknown spell type"


@spell_dispatcher.register(int)
def _handle_int(spell: int) -> str:
    return f"Damage spell: {spell} damage"


@spell_dispatcher.register(str)
def _handle_str(spell: str) -> str:
    return f"Enchantment: {spell}"


@spell_dispatcher.register(list)
def _handle_list(spell: list) -> str:
    return f"Multi-cast: {len(spell)} spells"


if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(nums, 'sum')}")
    print(f"Product: {spell_reducer(nums, 'product')}")
    print(f"Max: {spell_reducer(nums, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    print(spell_dispatcher(["fire", "ice", "thunder"]))
    print(spell_dispatcher(12.5))
