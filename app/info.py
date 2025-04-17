import sys
import os

def resource_path(relative_path):
    """Holt den absoluten Pfad zur Resource – funktioniert auch nach dem Einfrieren."""
    if hasattr(sys, '_MEIPASS'):
        # Wenn als Executable ausgeführt
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Im normalen Entwicklungsmodus
        return os.path.join(os.path.abspath("."), relative_path)

def license():
    with open(resource_path("LICENSE"), "r") as f:
        license_text = f.read()
        print('\n' + license_text)
    
    choice = input("Do you want to see more? [y/n]: ")

def main():
    print("Infos")
