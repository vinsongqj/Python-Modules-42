#!/usr/bin/env python3

class Plant:
    def __init__(self, name:    str, height:    int, plant_age:   int):
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def grow(self, cm:   int):
        self.height += cm

    def age(self, days: int):
        self.plant_age += days

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    init_height = rose.height
    print("=== Day 1 ===")
    print(rose.get_info())
    rose.grow(6)
    rose.age(6)
    print("=== Day 7 ===")
    print(rose.get_info())
    diff = rose.height - init_height
    print(f"Growth this week: +{diff}cm")
