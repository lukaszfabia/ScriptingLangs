import sys
from Parser import ParsedLog

def read_file():
    with open('C:/Users/ufabi/Desktop/ScriptingLangs/Lab1and2/tmp.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            log = ParsedLog(line.rstrip())
            if log.matched:
                yield log
            else:
                pass


def read_log():
    for line in sys.stdin:
        curr = ParsedLog(line.rstrip())
        if curr.matched:
            yield curr
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