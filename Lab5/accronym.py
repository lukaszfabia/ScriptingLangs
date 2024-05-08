from functools import reduce
from typing import *
import pytest

tests_cases: List[Tuple[List[str], str]] = (
    [
        (["hello", "world"], "HW"),
        (["hello", "world", "python"], "HWP"),
        (["this", "is", "a", "test"], "TIAT"),
        (["programming", "is", "fun"], "PIF"),
        (["python", "is", "awesome"], "PIA"),
        (["Zakład", "Utylizacji", "staruszków"], "ZUS"),
        (["spółka", "z", "ograniczoną", "odpowiedzialnością"], "SZOO"),
    ],
)


def accr(lst: Sequence[str]) -> str:
    """creates accronym from list of words uses tail recursion"""

    def aux(acc: str, rest: Sequence[str]) -> str:
        match rest:
            case []:
                return acc
            case [head, *tail]:
                return aux(acc + head[0].upper(), tail)

    return aux("", lst)


@pytest.mark.parametrize("lst, expected", tests_cases[0])
def test_accr(lst, expected):
    assert accr(lst) == expected
