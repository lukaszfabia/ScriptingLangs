import sys
from Parser import ParsedLog


def read_file(filename: str):
    with open(f"../ScriptingLangs/Lab1and2/{filename}", "r", encoding="UTF-8") as f:
        for line in f:
            log = ParsedLog(line.rstrip())
            if log.matched:
                yield log.tuple_repr()
            else:
                pass


def read_log():
    for line in sys.stdin:
        curr = ParsedLog(line.rstrip())
        if curr.matched:
            yield curr.tuple_repr()
        else:
            pass


def read_params(*args):
    """getting parameters from command line

    Returns:
        args: list of default parameters if there will be no parameters in line
    """
    if len(sys.argv) > 1:
        return sys.argv[1:]
    else:
        return args
