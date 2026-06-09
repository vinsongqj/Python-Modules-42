#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Caught a garden error: {self.message}"


class PlantError(GardenError):
    def __str__(self):
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __str__(self):
        return f"Caught WaterError: {self.message}"


def plant_error():
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(e)


def water_error():
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(e)
    print("")


def garden_error():
    print("Testing catching all garden errors...")
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print(e)
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print(e)
    print("")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    plant_error()
    print("Testing WaterError...")
    water_error()
    garden_error()
    print("All custom error types work correctly!")
