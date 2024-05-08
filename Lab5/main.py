from functools import reduce
from typing import *


def accronym(lst: List[str]) -> str:
    return reduce(lambda acc, word: acc + word[0].upper(), lst, "")
