from datetime import time
from iostream import *


def downloaded_at(logs, start: int, end: int) -> None:
    """prints logs that are between given time

    Args:
        * log (str): log from apache
        * start (int): start hour (hh:00:00)
        * end (int): end hour (hh:00:00)
    """
    start = time(start, 0, 0)
    end = time(end, 0, 0)
    for log in logs:
        time_: time = time(log.date_.hour, log.date_.minute, log.date_.second)
        if start > end:
            if not end < time_ and time_ < start:
                print(log)
        else:
            if end < time_ and time_ < start:
                print(log)


if __name__ == '__main__':
    # logs = list(read_log())
    params = read_params(22, 6)
    logs = list(read_file())
    downloaded_at(logs, start=int(params[0]), end=int(params[1]))