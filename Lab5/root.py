# 𝑦 ≥ 0 i |𝑦^2 − 𝑥| < 𝑒𝑝𝑠𝑖𝑙𝑜𝑛
from typing import *

import pytest


test_cases: Tuple[float, float, Optional[float]] = [
    (4, 0.0001, 2.0),
    (9, 0.000001, 3.0),
    (100, 0.000001, 10.0),
    (3, 0.1, 1.75),
    (0, 0.1, 0.0),
]


def root(x: float, precsion: float) -> Optional[float]:
    """compte the square root of a number

    Args:
        x (float): not negative number
        precsion (float): presicion of the result

    Returns:
        Optional[float]: result of the square root or None if x is negative
    """

    def aux(y: float):
        match abs(y**2 - x) < precsion and y >= 0:
            case True:
                return y
            case _:
                return aux(y - (y**2 - x) / (2 * y))

    match x >= 0:
        case True:
            return aux(x)
        case False:
            return None


@pytest.mark.parametrize("x, precision, expected", test_cases)
def test_root(x: float, precision: float, expected: Optional[float]):
    assert pytest.approx(root(x, precision)) == expected
