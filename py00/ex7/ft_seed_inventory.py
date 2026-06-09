def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = f"{seed_type.capitalize()} seeds:"
    if unit == "packets":
        print(f"{seed} {quantity} packets available")
    elif unit == "grams":
        print(f"{seed} {quantity} grams total")
    elif unit == "area":
        print(f"{seed} covers {quantity} square meters")
    else:
        print("Unknown unit type")
