def main(file_name: str) -> None:
    print("\n=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    try:
        file = open(file_name, 'r')

        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...\n")

        print("RECOVERED DATA:")

        content = file.read()
        print(content)

        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print(f"ERROR: Vault {file_name} not found.")
    except Exception as e:
        print(f"An unexpected corruption occurred: {e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    main("ancient_fragment.txt")
