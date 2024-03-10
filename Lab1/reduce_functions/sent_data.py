from preproccess_line.preproccess import *
import numpy as np
from reduce_functions.max_resource import update_max_resource

SENT_GB: float = 0.0


def update_amount_of_sent_data(log: str) -> None:
    global SENT_GB
    SENT_GB += gb_sent(log)


def getSentGb() -> float:
    return np.round(SENT_GB, 2)
