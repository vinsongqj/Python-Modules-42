import time
import functools
from typing import Any, Callable


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            print(f"Casting {func.__name__}...")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Spell completed in {end - start:.3f} seconds")
            return result
        except Exception:
            return "Spell failed"
    return wrapper


def retry_spell(retries: int = 3):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < retries - 1:
                        print(f"Spell failed, retrying... "
                              f"(attempt {i + 1}/{retries})")
            print(f"Spell casting failed after {retries} attempts")
            return f"Waaaaaaagh {func.__name__} !"
        return wrapper
    return decorator


class MageGuild:
    def __init__(self, size_limit: int):
        self.size_limit = size_limit

    @staticmethod
    def is_valid_name(name: str) -> bool:
        try:
            return name.isalpha() and len(name) > 3
        except (AttributeError, TypeError):
            return False

    def cast_with_limit(self, spell_name: str, power: int) -> str:
        try:
            if power <= self.size_limit:
                return f"Successfully cast {spell_name} with {power} power"
            return "Insufficient power for this spell"
        except (TypeError, ValueError):
            return "Invalid power level"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(retries=3)
def spelled() -> str:
    raise Exception("Mana leak")


if __name__ == "__main__":
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    print(spelled())

    print("\nTesting MageGuild...")
    guild = MageGuild(20)
    print(MageGuild.is_valid_name("Albus"))
    print(MageGuild.is_valid_name("123"))
    print(guild.cast_with_limit("Lightning", 15))
    print(guild.cast_with_limit("Big Bang", 50))
