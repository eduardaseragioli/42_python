def creation(file_name: str, content: str) -> None:
    """Create a new archive file and write preservation data to it.

    Opens a file for writing, inscribes the provided content,
    and ensures proper file closure. Handles permission errors
    and other exceptions gracefully.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    file = None
    try:
        file = open(file_name, "w")

        print(f"\nInitializing new storage unit: {file_name}")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")

        file.write(content)
        print(content)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

    except PermissionError:
        print(f"ERROR: Security protocols deny write access to '{file_name}'")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to create archive: {e}")
    finally:
        if file:
            file.close()


def main() -> None:
    """
    Main function to demonstrate archive creation.
    """
    file_name: str = "new_discovery.txt"
    content: str = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    )
    creation(file_name, content)


if __name__ == "__main__":
    main()
