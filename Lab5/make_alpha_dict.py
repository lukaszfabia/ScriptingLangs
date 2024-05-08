import re
from typing import Dict, List
import pytest


test_cases = [
    (
        "ala ma kota a kot ma ale",
        {
            "a": ["ala", "ma", "kota", "a", "ma", "ale"],
            "m": ["ma", "ma"],
            "k": ["kota", "kot"],
            "o": ["kota", "kot"],
            "t": ["kota", "kot"],
            "l": ["ala", "ale"],
            "e": ["ale"],
        },
    ),
    ("on i ona", {"o": ["on", "ona"], "n": ["on", "ona"], "i": ["i"], "a": ["ona"]}),
    ("heh xd", {"h": ["heh"], "e": ["heh"], "x": ["xd"], "d": ["xd"]}),
    ("", {}),
]


def make_dict(s: str) -> Dict[str, List[str]]:
    return {
        c: list(filter(lambda x: c in x, re.split(r"\s+", s)))
        for c in filter(lambda x: x.isalpha(), s)
    }


@pytest.mark.parametrize("input, expected", test_cases)
def test_make_dict(input, expected):
    assert make_dict(input) == expected
