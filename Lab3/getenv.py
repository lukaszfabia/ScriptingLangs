from functools import reduce
import sys
import os


def print_all_env_vars(term: callable) -> None:
    for name, value in sorted(os.environ.items()):
        if term(name):
            print(f"{name}={value}")


def term(name: str) -> bool:
    if len(sys.argv) == 1:
        return True
    else:
        return any(curr.upper() in name for curr in sys.argv[1:])


if __name__ == "__main__":
    if sys.argv[1] in ("--help", "-h"):
        print("Usage: getenv.py optional: [word1] [word2] ... [wordN]")
        print("Example: python getenv.py homebrew")
        print("Prints all environment variables that contain any of the given words")
    else:
        print_all_env_vars(term)
