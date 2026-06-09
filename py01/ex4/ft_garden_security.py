#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name:    str, height:    int, age:   int):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, value: int):
        if value < 0:
            print(f"\nInvalid operation attempted: height {value}cm"
                  f" [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, value):
        if value < 0:
            print(f"\nInvalid operation attempted: age {value} days"
                  f" [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self):
        return f"{self.__height}cm"

    def get_age(self):
        return f"{self.__age} days"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 0, 0)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name}"
          f"({rose.get_height()}, {rose.get_age()})")
