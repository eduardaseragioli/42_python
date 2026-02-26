import sys


def main() -> None:
    """
    Demonstrate proper usage of system communication streams.

    Collects archivist information via stdin and demonstrates
    proper channel separation by routing messages to stdout
    (standard messages) and stderr (alert messages).
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        input_id = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")

    except (KeyboardInterrupt, EOFError):
        print("\n[System] An error occured, try again", file=sys.stderr)
    else:
        sys.stdout.write(
            f"\n[STANDARD] Archive status from {input_id}: {status}\n")
        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
