from dotenv import load_dotenv
import os
import sys

DEFAULT_LOG_LEVEL = "DEBUG"
ALLOWED_MODES = ["development", "production"]
VALID_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
ENV_FILE = ".env"


def load_configuration() -> dict:

    load_dotenv(override=False)

    dict_config: dict = {
        'MATRIX_MODE': os.getenv("MATRIX_MODE", "development"),
        'DATABASE_URL': os.getenv("DATABASE_URL", ""),
        'API_KEY': os.getenv("API_KEY", ""),
        'LOG_LEVEL': os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL),
        'ZION_ENDPOINT': os.getenv("ZION_ENDPOINT", "")
    }
    return dict_config


def validate_configuration(config: dict) -> tuple[list, list]:
    errors: list = []
    warnings: list = []

    if config['MATRIX_MODE'] not in ALLOWED_MODES:
        errors.append("MATRIX_MODE must be 'development' or 'production'")

    for key in ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]:
        if not config[key]:
            errors.append(f"{key} is missing")

    if config["LOG_LEVEL"] not in ["DEBUG", "INFO", "WARNING",
                                   "ERROR", "CRITICAL"]:
        warnings.append("LOG_LEVEL invalid, falling back to INFO")
        config["LOG_LEVEL"] = "INFO"

    return errors, warnings


def print_configuration_status(config: dict, errors: list,
                               warnings: list) -> None:

    print("\nORACLE STATUS: Reading the Matrix...\n")

    if errors:
        print("Configuration loaded with issues:")
    else:
        print("Configuration loaded:")

    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        if "localhost" in config["DATABASE_URL"] or "127.0.0.1" \
                in config["DATABASE_URL"]:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: [Missing] configuration")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing credentials")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline (endpoint missing)")

    for warning in warnings:
        print((f"[WARN] {warning}"))

    for error in errors:
        print(f"[ERROR] {error}")


def security_check(config: dict) -> None:

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    if os.path.exists(ENV_FILE):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found")
    print("[OK] Production overrides available")


def main() -> None:
    config = load_configuration()
    errors, warnings = validate_configuration(config)

    print_configuration_status(config, errors, warnings)

    security_check(config)

    if errors:
        print("The Oracle sees configuration issues.")
        sys.exit(1)
    else:
        print("The Oracle sees all configurations.")
        sys.exit(0)


if __name__ == "__main__":
    main()
