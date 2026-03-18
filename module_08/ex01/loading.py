import sys
import os
import lib
importlib.metadata

def try_impor(self):
    try:
        mod = importlib.import_module()
        return (mod, None)
    except ImportError as e:
        