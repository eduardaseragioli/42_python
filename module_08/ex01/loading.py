import sys
import os
import lib
importlib.metadata


def get_package_version(package_name):
    try:
        version = importlib.metadata.version(package_name)
        return version
    except:
        return "unknown"


def try_import(self) -> None:
    try:
        mod = importlib.import_module(package_name)
        return (True, mod)
    except ModuleNotFoundError as e:
        return (False, None)


def check_dependencies() -> None:
    status: dict = {}

    for packeds in required_packages:
        module = try_import(packeds)
        if :
            version = get_package_version(packeds)
            status[packeds] = {
                'installed': True,
                'version': version,
                'required': True,
                'module': module
            }
        else:
            status[packeds] = {
                'installed': False,
                'version': None,
                'required': True,
                'module': None
            }
    
    for packeds in optional_packages:
        module = try_import(packeds)

        if :
            version = get_package_version(packeds)
            status[packeds] = {
                'installed': True,
                'version': version,
                'required': False,
                'module': module
            }
        else:
            status[packeds] = {
                'installed': False,
                'version': None,
                'required': False,
                'module': None
            }
    return status

def print_dependency_report(status) -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

    for package, info in status:
        if info.installed == True:
            if package == "pandas":
                msg = "Data manipulation ready"
            if package == "numpy":
                msg = " Network access ready"
            elif package == 