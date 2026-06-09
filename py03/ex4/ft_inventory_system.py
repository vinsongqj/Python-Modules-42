#!/usr/bin/env python3

import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory = dict()
    try:
        if not args:
            print("No arguments provided. (Usage: python3 "
                  "ft_inventory_system.py item:qty item2:qty)")
            return
        for arg in args:
            if ':' in arg:
                key, value = arg.split(':', 1)
                inventory.update({key: int(value)})
            else:
                print(f"Warning: {arg} is missing a colon.")
        total_items = sum(inventory.values())
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {len(inventory)}")
        print("\n=== Current Inventory ===")
        items = [[key, value] for key, value in inventory.items()]
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][1] < items[j+1][1]:
                    items[j], items[j+1] = items[j+1], items[j]
        for key, value in items:
            percentage = (float(value) / total_items) * 100
            label = "unit" if value == 1 else "units"
            print(f"{key}: {value} {label} ({percentage:.1f}%)")
        print("\n=== Inventory Statistics ===")
        max_key = None
        max_value = -1
        for key, value in inventory.items():
            num_value = int(value)
            if num_value > max_value:
                max_value = num_value
                max_key = key
        max_label = "unit" if max_value == 1 else "units"
        print(f"Most abundant: {max_key}: ({max_value} {max_label})")
        min_key = None
        min_value = None
        is_first = True
        for key in inventory:
            current_value = int(inventory[key])
            if is_first or current_value < min_value:
                min_value = current_value
                min_key = key
                is_first = False
        min_label = "unit" if min_value == 1 else "units"
        print(f"Least abundant: {min_key}: ({min_value} {min_label})")
        print("\n=== Item Categories ===")
        moderate = dict()
        scarce = dict()
        for key, value in inventory.items():
            val = int(value)
            if val >= 5:
                moderate.update({key: val})
            else:
                scarce.update({key: val})
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")
        print("\n=== Management Suggestions ===")
        restock = 2
        output = ""
        for key, value in inventory.items():
            if int(value) < restock:
                if output == "":
                    output = key
                else:
                    output = output + ", " + key
        if output:
            print(f"Restock needed: {output}")
        print("\n=== Dictionary Properties Demo ===")
        key_str = list(inventory.keys())
        print(f"Dictionary keys: {key_str} ")
        value_str = list(inventory.values())
        print(f"Dictionary values: {value_str} ")
        sample = 'sword'
        exist = inventory.get(sample, 0)
        print(f"Sample lookup - '{sample}' in inventory: {exist}")
    except ValueError:
        print("Error: Quantities must be integers")
    except ZeroDivisionError:
        print("Error: Inventory is empty, cannot calculate percentages.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ft_inventory_system()
