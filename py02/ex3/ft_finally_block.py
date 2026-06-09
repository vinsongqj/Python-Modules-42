#!/usr/bin/env python3

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plants)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    plants = ["tomato", None, "carrots"]
    plants[1]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
