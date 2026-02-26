def crisis_response(files: list[str]) -> None:
    """
    Handle crisis scenarios for multiple archive files.

    Attempts to access each file and handles different error types
    gracefully using the with statement and exception handling.

    Args:
        files: List of file paths to attempt accessing

    Returns:
        None
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    for file_name in files:
        if file_name == "standard_archive.txt":
            print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
        else:
            print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")

        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print(f"SUCCESS: Archive recovered - ``{content}''")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception as e:
            print(f"An unexpected error occurred {e}.")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


def main() -> None:
    """
    Main function to test crisis response scenarios.

    Tests three different scenarios:
    - Missing archive (FileNotFoundError)
    - Restricted access (PermissionError)
    - Successful access

    Returns:
        None
    """
    files: list[str] = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    crisis_response(files)


if __name__ == "__main__":
    main()
