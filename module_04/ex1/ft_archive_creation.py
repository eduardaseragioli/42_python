def main(file_name: str, content: str) -> None:

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    try:
        file = open(file_name, "w")

        print(f"\nInitializing new storage unit: {file_name}")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")

        file.write(content)
        print(content)

        print("\n Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

    except PermissionError:
        print(f"ERROR: Security protocols deny write access to '{file_name}'")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to create archive: {e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    file_name = " new_discovery.txt"
    content = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    )
    main(file_name, content)