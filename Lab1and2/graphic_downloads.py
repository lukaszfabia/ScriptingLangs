from iostream import *
from numpy import round

ACCEPTED_EXTENSIONS = ("gif", "jpg", "jpeg", "xbm", "png")


def get_ratio(logs):
    """graphic/non_graphic ratio + graphic

    Args:
        logs (ParseLog): log objects

    Returns:
        float: ratio
    """
    graphic = non_graphic = 0
    for log in logs:
        if log[3].endswith(ACCEPTED_EXTENSIONS):
            graphic += 1
        else:
            non_graphic += 1
    return round(graphic / non_graphic, 2)


if __name__ == "__main__":
    logs = list(read_log())
    # logs = list(read_file())
    print(get_ratio(logs))
