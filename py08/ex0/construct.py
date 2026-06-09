#!/usr/bin/env python3

import sys
import os
import site


def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_matrix_status() -> None:
    python_executable: str = sys.executable
    venv_active: bool = is_venv()

    # if outside the matrix
    if not venv_active:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate   # On Windows")
        print("\nThen run this program again.")

    # if inside the matrix
    else:
        venv_name: str = os.path.basename(sys.prefix)
        pkg_path: str = site.getsitepackages()

        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"\nPackage installation path:\n {pkg_path}")


if __name__ == "__main__":
    try:
        get_matrix_status()
    except Exception as e:
        print(f"An error occurred: {e}")
