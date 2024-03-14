from preproccess import *
import numpy as np
from iostream import read_std
from present_data import print_output

SENT_GB: float = 0.0


def update_amount_of_sent_data(log: str) -> None:
    global SENT_GB
    SENT_GB += gb_sent(log)


def get_sent_gb() -> float:
    return np.round(SENT_GB, 2)


if __name__ == '__main__':
    read_std(update_amount_of_sent_data)
    print_output(SENT_GB=f'{get_sent_gb()} GB')
