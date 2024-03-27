import sys
import os
from typing import Iterable


def filter_files(directory: str) -> Iterable[str]:
    for file in os.listdir(directory):
        absolute_path_to_file = os.path.join(directory, file)
        if os.path.isfile(absolute_path_to_file) and os.access(
            absolute_path_to_file, os.X_OK
        ):
            print(f"\t{file}")


def print_all_path_dir(flag="") -> None:
    path = os.environ.get("PATH").split(os.pathsep)
    for dir in path:
        if os.path.exists(dir) and os.path.isdir(dir):
            print(f"\n{dir}:")
            if "-e" in flag:
                filter_files(dir)


if __name__ == "__main__":
    print_all_path_dir(str(sys.argv[1:]))
