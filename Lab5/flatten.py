from typing import *

import pytest

test_cases = [
    ([1, [2, 3], [[4, 5], 6]], [1, 2, 3, 4, 5, 6]),
    ([[[[[[[[1]]]]]]]], [1]),
    ([[], []], []),
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
            [16, 17, 18],
            [19, 20, 21],
            [22, 23, 24],
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
        ],
    ),
]


def flatten(lst: List[Any]) -> List[Any]:
    """programming paradigms - flatten list"""
    match lst:
        case []:
            return []
        case [head, *tail]:
            match isinstance(head, (list, tuple)):
                case True:
                    return flatten(head) + flatten(tail)
                case _:
                    return [head] + flatten(tail)


@pytest.mark.parametrize("input, expected", test_cases)
def test_flatten(input: List[Any], expected: List[Any]):
    assert flatten(input) == expected
