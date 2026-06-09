#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importlib.metadata


def check_dependencies() -> None:
    libs = ["pandas", "numpy", "matplotlib"]
    print("Checking dependencies:")
    for lib in libs:
        try:
            version = importlib.metadata.version(lib)
            print(f"[OK] {lib} ({version}) - Ready")
        except importlib.metadata.PackageNotFoundError:
            print(f"[ERROR] {lib} is missing from the Matrix!")
            sys.exit(1)


def process_matrix_data(file_path: str) -> pd.DataFrame | None:
    try:
        df: pd.DataFrame = pd.read_csv(file_path)
        point_count: int = len(df)

        print("\nAnalyzing Matrix data...")
        print(f"Processing {point_count} data points...")

        return df

    except Exception:
        return None


def generate_matrix_viz(df: pd.DataFrame, output_file: str) -> None:

    print("Generating visualization...")

    plt.figure(figsize=(8, 6))
    plt.hist(np.random.randn(1000), bins=30, color='green', alpha=0.7)
    plt.title("Matrix Data Distribution")
    plt.savefig(output_file)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    check_dependencies()

    data: pd.DataFrame | None = process_matrix_data("data.csv")

    if data is not None:
        generate_matrix_viz(data, "matrix_analysis.png")
    else:
        print("[ERROR] Could not find data.csv")


if __name__ == "__main__":
    main()
