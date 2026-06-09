#!/usr/bin/env python3

def ft_crisis_response(file: str) -> None:
    try:
        with open(file, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting to access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
        return
    except PermissionError:
        print(f"CRISIS ALERT: Attempting to access to '{file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
        return
    print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
    with open(file, "r") as f:
        content = f.read()
        print(f"SUCCESS: Archive recovered - ''{content}''")
        print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    ft_crisis_response("lost_archive.txt")
    ft_crisis_response("classified_vault.txt")
    ft_crisis_response("standard_archive.txt")
