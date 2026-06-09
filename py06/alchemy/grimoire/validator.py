#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    if any(element in ingredients.lower() for element in valid):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
