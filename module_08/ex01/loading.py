import sys
import importlib
import warnings
from importlib import metadata


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]
OPTIONAL_PACKAGES = ["requests"]


def get_package_version(package_name: str) -> str:
    try:
        version = metadata.version(package_name)
        return version
    except metadata.PackageNotFoundError:
        return "unknown"


def try_import(package_name: str) -> tuple[bool, object | None]:
    try:
        module = importlib.import_module(package_name)
        return True, module
    except (ModuleNotFoundError, ImportError):
        return False, None


def check_dependencies() -> dict[str, dict[str, object]]:
    status: dict[str, dict[str, object]] = {}
    all_packages = [(name, True) for name in REQUIRED_PACKAGES]
    all_packages += [(name, False) for name in OPTIONAL_PACKAGES]

    for package_name, required in all_packages:
        installed, module = try_import(package_name)
        status[package_name] = {
            "installed": installed,
            "version": (
                get_package_version(package_name)
                if installed else None
            ),
            "required": required,
            "module": module,
        }
    return status




def print_dependency_report(status: dict[str, dict[str, object]]) -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    messages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }

    for package, info in status.items():
        if info["installed"]:
            print(f"[OK] {package} ({info['version']}) - {messages[package]}")
        elif info["required"]:
            print(f"[MISSING] {package} - Required dependency not installed")
        else:
            print(f"[OPTIONAL] {package} - Not installed")


def get_missing_required(status: dict[str, dict[str, object]]) -> list[str]:
    missing: list[str] = []
    for package, info in status.items():
        if info["required"] and not info["installed"]:
            missing.append(package)
    return missing


def print_install_instructions(missing: list[str]) -> None:
    if not missing:
        return

    print("\nWARNING: Missing required dependencies:")
    print(", ".join(missing))
    print("\nInstall with pip:")
    print("pip install -r requirements.txt")
    print("\nInstall with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def print_manager_comparison() -> None:
    print("\nDependency manager comparison:")
    print("- pip uses requirements.txt")
    print("- Poetry uses pyproject.toml (+ lockfile)")
    print("- Poetry creates/reuses isolated env automatically")


def run_analysis(status: dict[str, dict[str, object]]) -> None:
    np = status["numpy"]["module"]
    pd = status["pandas"]["module"]
    warnings.filterwarnings(
        "ignore",
        message="Unable to import Axes3D.*",
        category=UserWarning,
    )
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    data_points = 1000

    x = np.arange(data_points)
    y = np.random.normal(loc=50, scale=10, size=data_points)

    df = pd.DataFrame({"index": x, "value": y})
    print(f"Processing {len(df)} data points...")

    plt.figure(figsize=(8, 4))
    plt.plot(df["index"], df["value"], linewidth=1)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Generating visualization...\n")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    status = check_dependencies()
    print_dependency_report(status)
    print_manager_comparison()

    missing = get_missing_required(status)
    if missing:
        print_install_instructions(missing)
        sys.exit(1)

    run_analysis(status)


if __name__ == "__main__":
    main()
