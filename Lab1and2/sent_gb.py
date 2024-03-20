from iostream import *
from numpy import round


def sent_gb(logs):
    total_bytes = sum(log[5] for log in logs)
    return total_bytes / 1024**3


if __name__ == "__main__":
    logs = list(read_log())
    # logs = list(read_file())
    print(round(sent_gb(logs), 2), "GB")
