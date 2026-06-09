#!/usr/bin/env python3

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
file = "ancient_fragment.txt"
print(f"Accessing Storage Vault: {file}")
try:
    f = open(file, "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    read = f.read()
    print(read)
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
finally:
    if f:
        f.close()
