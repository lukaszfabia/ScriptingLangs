from preproccess import get_date_and_time
from iostream import *
from datetime import time


def resources_downloaded_between(log: str, start: int, end: int) -> None:
    """prints logs that are between given time

    Args:
        * log (str): log from apache
        * start (int): start hour (hh:00:00)
        * end (int): end hour (hh:00:00)
    """
    time_: time = get_date_and_time(log)[1]
    start = time(start, 0, 0)
    end = time(end, 0, 0)
    if start > end:
        if not end < time_ and time_ < start:
            print(log)
    else:
        if end < time_ and time_ < start:
            print(log)


if __name__ == '__main__':
    params = read_params(22, 6)
    read_std(resources_downloaded_between,
             start=int(params[0]), end=int(params[1]))
