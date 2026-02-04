import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def visualize_structure(path: Path, level: int = 0):
    """
    Recursively prints directory structure with colored output.

    Directories are printed in blue.
    Files are printed in green.
    """
    for item in path.iterdir():
        indent = '    ' * level
        if item.is_dir():
            print(f"{indent}{Fore.BLUE + item.name}")
            visualize_structure(item, level + 1)
        elif item.is_file():
            print(f"{indent}{Fore.GREEN + item.name}")
            
def main():
    """
    Entry point of the script.
    Reads directory path from command line arguments.
    """
    if len(sys.argv) < 2:
        return
    
    dir_path = Path(sys.argv[1])
    if not dir_path.exists():
        print(Fore.RED + "Error: The path does not exist")
        return

    if not dir_path.is_dir():
        print(Fore.RED + "Error: The specified path is not a directory.")
        return
    visualize_structure(dir_path)

if __name__ == "__main__":
    main()
