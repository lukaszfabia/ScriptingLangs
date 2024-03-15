from functools import reduce
from iostream import *


def get_max_bytes(logs: list):
    res = reduce(lambda current_max, curr: current_max if current_max.bytes_ > curr.bytes_ else curr, logs).bytes_
    return round(res/1024**3, 7)


if __name__ == '__main__':
    # logs = list(read_log())
    logs = list(read_file())
    print(get_max_bytes(logs), "GB")