import colorama
from colorama import Fore
import sys
from pathlib import Path

colorama.init(autoreset=True)

def parse_folder(directory_path, indent=""):                            
    for el in directory_path.iterdir():
        if el.is_dir():                                                         # is this directory ? tell us name of 
            print(indent + Fore.YELLOW + f"Directory: {el.name}/")
            parse_folder(el, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"File: {el.name}")                     # is this file ? tell us name of 

directory_path = Path(sys.argv[1])                                              # get directory path from terminal and check /n
if not directory_path.exists() or not directory_path.is_dir():                  # if it exist
    print(Fore.MAGENTA + "Invalid directory path.")                             # colored msg if not
    sys.exit(1)

parse_folder(directory_path)
