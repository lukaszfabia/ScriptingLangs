from functools import reduce
from iostream import *


def get_max_bytes(logs: list):
    res = reduce(
        lambda current_max, curr: current_max if current_max[5] > curr[5] else curr,
        logs,
    )[5]
    return res


if __name__ == "__main__":
    logs = list(read_log())
    # logs = list(read_file())
    print(get_max_bytes(logs), "B")
