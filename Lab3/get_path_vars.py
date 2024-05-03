import sys
import os
from typing import Iterable


def _filter_files(directory: str) -> None:
    """### filter files in a directory, gets executable files

    Args:
        * directory (str): path to directory
    """
    for file in os.listdir(directory):
        absolute_path_to_file = os.path.join(directory, file)
        if os.path.isfile(absolute_path_to_file) and os.access(
            absolute_path_to_file, os.X_OK
        ):
            print(f"\t{file}")


def print_all_path_dir(flag: str = "") -> None:
    """## prints all directories in the PATH environment variable

    Args:
        * flag (str, optional): defines if we want to print exe files. Accepts "-e". Defaults to "".
    """
    path = os.environ.get("PATH").split(os.pathsep)
    for dir in path:
        if os.path.exists(dir) and os.path.isdir(dir):
            print(f"\n{dir}:")
            if "-e" in flag:
                _filter_files(dir)


if __name__ == "__main__":
    print_all_path_dir(str(sys.argv[1:]))
