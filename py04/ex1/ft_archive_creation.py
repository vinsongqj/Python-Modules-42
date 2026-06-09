#!/usr/bin/env python3

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
file = "new_discovery.txt"
print(f"Initializing new storage unit: {file}")
try:
    f = open(file, "w")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    content = ("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee")
    f.write(content)
    print(content)
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file}' ready for long term preservation.")
except Exception as e:
    print(e)
finally:
    if f:
        f.close()
