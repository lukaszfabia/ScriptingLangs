from typing import *
import pytest


test_cases: List[Tuple[List[int], float]] = (
    [
        ([1, 1, 19, 2, 3, 4, 4, 5, 1], 3),
        ([6, 4, 2, 4, 4], 4),
        ([5, 8, -1, 6, 6, 1, 10], 6),
        ([7, 8, 3, 4, 9, 2], 5.5),
    ],
)


def median(lst: List[int]) -> float:
    lst.sort()  # a zmienie sie liste i chuj
    match len(lst) % 2 == 0:
        case True:
            return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
        case _:
            return lst[len(lst) // 2]


print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))


@pytest.mark.parametrize("lst, expected", test_cases[0])
def test_median(lst, expected):
    assert median(lst) == expected
