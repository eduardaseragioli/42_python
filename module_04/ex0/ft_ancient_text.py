def main(file_name: str) -> None:
    """
    Recover and display data from an ancient archive file.
    Opens a file, reads its contents, and displays the recovered data.
    Handles file access errors and ensures proper file closure.
    """
    print("\n=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    file = None
    try:
        file = open(file_name, 'r')

        print(f"\nAccessing Storage Vault: {file_name}")
        print("Connection established...\n")

        print("RECOVERED DATA:")

        content = file.read()
        print(content)

        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print(f"ERROR: Vault {file_name} not found.")
    except Exception as e:
        print(f"An unexpected corruption occurred: {e}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    main("ancient_fragment.txt")
