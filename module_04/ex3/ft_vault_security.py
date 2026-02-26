def main(file_extraction: str, file_preservation: str) -> None:
    """
    Demonstrate secure vault operations using the with statement.
    Performs two secure operations:
    1. SECURE EXTRACTION - reads classified data from a vault
    2. SECURE PRESERVATION - writes new security protocols to a vault
    The with statement ensures automatic vault sealing (file closing)
    even if errors occur, preventing data corruption and resource leaks
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")

    try:
        with open(file_extraction, 'r') as file:
            print("Vault connection established with failsafe protocols\n")

            print("SECURE EXTRACTION:")
            content = file.read()
            print(content)

        with open(file_preservation, 'w') as file:
            print("\nSECURE PRESERVATION:")

            text: str = "[CLASSIFIED] New security protocols archived"
            file.write(text)
            print(text)

            print("Vault automatically sealed upon completion\n")

            print("All vault operations completed with maximum security.")

    except Exception as e:
        print(f"CRITICAL: Unexpected security breach: {e}")


if __name__ == "__main__":
    main('classified_data.txt', 'security_protocols.txt')
