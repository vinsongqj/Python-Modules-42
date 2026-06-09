#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days,"
              f" {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,"
              f" {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        shade = int((self.trunk_diameter * 3.14) / 2)
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest\n{self.name}"
              f" is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    r = Flower("rose", 25, 30, "red")
    r.bloom()
    o = Tree("Oak", 500, 1825, 50)
    o.produce_shade()
    t = Vegetable("tomato", 80, 90, "summer", "vitamin C")
