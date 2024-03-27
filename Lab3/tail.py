import sys
import os


def get_n(flag: str) -> int:
    if "-l" in flag or "--lines" in flag:
        return int(flag.rstrip().split("=")[1])
    else:
        return 10


def tail(contents: str, flag="") -> None:
    lines = contents.splitlines()
    for line in lines[-get_n(flag) :]:
        print(line)


def preprocess_line(args: list):
    if len(args) == 1:
        tail(contents=sys.stdin.read())
    elif "." in sys.argv[1]:
        with open(args[1], "r") as file:
            tail(file.read())
    else:
        tail(contents=sys.stdin.read(), flag=str(args[1]))


if __name__ == "__main__":
    preprocess_line(sys.argv)
