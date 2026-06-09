#!/usr/bin/env python3

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...\n"
      "Vault connection established with failsafe protocols")
print("\nSECURE EXTRACTION:")
with open("classified_data.txt", "r") as f:
    content = f.read()
    print(content)
print("\nSECURE PRESERVATION:")
with open("security_protocols.txt") as f:
    content = f.read()
    print(content)
print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
