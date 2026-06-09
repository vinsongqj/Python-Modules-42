#!/usr/bin/env python3

class GardenError(Exception):
    pass


class ResourceError(GardenError):
    pass


class ValidationError(GardenError):
    pass


class Plant:
    def __init__(self, name, water_lvl, sun_lvl):
        if not name:
            raise ValidationError("Plant name cannot be empty!")
        self.name = name
        self.water = water_lvl
        self.sun = sun_lvl

    def check_health(self):
        if self.water > 10:
            raise ResourceError(f"Water level {self.water} is "
                                f"too high (max 10)")
        if self.water < 1:
            raise ResourceError(f"Water level {self.water} is too low (max 1)")
        return f"{self.name}: healthy (water: {self.water}, sun: {self.sun})"


class GardenManager():
    def __init__(self):
        self.plants = []
        self.water_lvl = 100

    def add_plant(self, name, water, sun):
        try:
            new_plant = Plant(name, water, sun)
            self.plants = self.plants + [new_plant]
            print(f"Added {name} successfully")
        except ValidationError as e:
            print(f"Error adding plant: {e}")

    def water_plant(self):
        try:
            if self.water_lvl < 10:
                raise GardenError("Not enough water in tank")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
                self.water_lvl -= 5
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")

    def check_plant_health(self):
        print("\nChecking plant health...")
        for plant in self.plants:
            try:
                print(plant.check_health())
            except ResourceError as e:
                print(f"Error checking {plant.name}: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    gm = GardenManager()
    print("Adding plants to garden...")
    gm.add_plant("tomato", 5, 8)
    gm.add_plant("lettuce", 15, 5)
    gm.add_plant("", 0, 0)
    print("\nWatering plants...\nOpening watering system")
    try:
        gm.water_plant()
    finally:
        print("Closing watering system (cleanup)")
    gm.check_plant_health()
    print("\nTesting error recovery...")
    gm.water_lvl = 5
    gm.water_plant()
    print("\nGarden management system test complete!")
