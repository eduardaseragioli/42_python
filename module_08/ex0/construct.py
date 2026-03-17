import sys
import os
import site


def is_in_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


def get_env_name() -> str:
    env_path = sys.prefix
    return os.path.basename(env_path)


def get_site_packages_path() -> str:
    site.getsitepackages()

    for path in paths:
        if "site-packages" in path:
            return path
        else:
            raise
    return path


def print_outside_message() -> str:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {}")
    print(f"Virtual Environment: {}")

    print("WARNING: You're in the global environment!")