#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    argc = len(sys.argv)
    received = argc - 1
    i = 1
    try:
        if received < 1:
            print("No arguments provided!")
            print(f"Program name: {sys.argv[0]}")
        else:
            print(f"Program name: {sys.argv[0]}")
            print(f"Arguments received: {received}")
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    except Exception as e:
        print(f"Error: {e}")
    print(f"Total arguments: {argc}\n")


if __name__ == "__main__":
    ft_command_quest()
