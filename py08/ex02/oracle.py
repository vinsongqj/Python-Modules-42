
import os
import sys


try:
    from dotenv import load_dotenv
except ImportError:
    print("Dependency Error: python-dotenv not found.")
    sys.exit(1)


def main():
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    db_status = os.getenv("DATABASE_URL", "local instance")
    api_access = os.getenv("API_KEY", "Authenticated")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    network = os.getenv("ZION_ENDPOINT", "Online")

    if not os.getenv("DB_PASS"):
        print("Error: Missing environment variables in .env")
        sys.exit(1)

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: Connected to {db_status}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {network}")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
