import sys
import os
import site


def is_in_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


def get_env_name() -> str:
    if is_in_venv():
        return os.path.basename(sys.prefix)
    return "None detected"


def get_site_packages_path() -> str:
    try:
        paths = site.getsitepackages()
        return paths[0]
    except Exception as e:
        return f"Error: {e}"


def print_outside_message() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_env_name()}")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")

    print("\nThen run this program again.")


def print_inside_message() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_env_name()}")
    print(f"Environment Path: {sys.prefix}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(get_site_packages_path())


def main() -> None:
    if is_in_venv():
        print_inside_message()
    else:
        print_outside_message()


if __name__ == "__main__":
    main()
