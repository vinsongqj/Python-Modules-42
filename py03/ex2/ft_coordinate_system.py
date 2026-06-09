#!/usr/bin/env python3

import math


def calculate_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> float:
    try:
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return distance
    except (ValueError, TypeError):
        return 0.0


def parse_coords(coord: str) -> tuple[int, int, int] | None:
    try:
        parts = coord.split(",")
        result = tuple(int(x) for x in parts)
        _x, _y, _z = result
        return result
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
        return None


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    pos1 = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {pos1}")
    distance = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {distance:.2f}")
    valid_str = "3,4,0"
    print(f'\nParsing coordinates: "{valid_str}"')
    pos2 = parse_coords(valid_str)
    if pos2:
        print(f"Parsed position: {pos2}")
        d2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {float(d2):.1f}")
    invalid_str = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_str}"')
    parse_coords(invalid_str)
    if pos2:
        print("\nUnpacking demonstration:")
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
