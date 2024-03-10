from preproccess_line.preproccess import *
from numpy import round
ACCEPTED_EXTENSIONS = ('gif', 'jpg', 'jpeg', 'xbm')

GRAPHIC: int = 0
NON_GRAPHIC: int = 0


def update_graphic_downloads(log: str) -> None:
    path = get_path(log)
    if path.endswith(ACCEPTED_EXTENSIONS):
        global GRAPHIC
        GRAPHIC += 1
    else:
        global NON_GRAPHIC
        NON_GRAPHIC += 1


def get_ratio_of_graphic_downloads() -> float:
    return round(GRAPHIC / (GRAPHIC + NON_GRAPHIC), 2)
