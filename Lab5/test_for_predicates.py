import pytest

from predicates import forall, exists, atleast, atmost


@pytest.mark.parametrize(
    ["pred", "iterable", "expected"],
    [
        (lambda x: x % 2 == 0, [1, 2, 3, 4], False),
        (lambda x: x % 2 == 0, [2, 4, 6, 8], True),
        (lambda x: x % 2 == 0, [], True),
    ],
)
def test_forall(pred, iterable, expected):
    assert forall(pred, iterable) == expected


@pytest.mark.parametrize(
    ["pred", "iterable", "expected"],
    [
        (lambda x: x % 2 == 0, [1, 2, 3, 4], True),
        (lambda x: x % 2 == 0, [1, 3, 5, 7], False),
        (lambda x: x % 2 == 0, [], False),
    ],
)
def test_exists(pred, iterable, expected):
    assert exists(pred, iterable) == expected


@pytest.mark.parametrize(
    "n, pred, iterable, expected",
    [
        (3, lambda x: x > 0, [1, 2, 3, 4, 5], True),
        (2, lambda x: x > 0, [-1, 2, -3, 4, 5], True),
        (2, lambda x: x % 2 == 0, [1, 3, 5], False),
        (0, lambda x: x % 2 == 0, [], True),
        (3, lambda x: x % 2 == 0, [1, 2, 3, 4], False),
    ],
)
def test_atleast(n, pred, iterable, expected):
    assert atleast(n, pred, iterable) == expected


@pytest.mark.parametrize(
    "n, pred, iterable, expected",
    [
        (3, lambda x: x > 0, [1, 2, 3, 4, 5], False),
        (2, lambda x: x > 0, [-1, 2, -3, 4, 5], False),
        (2, lambda x: x % 2 == 0, [1, 3, 5], True),
        (0, lambda x: x % 2 == 0, [1, 3, 5], True),
    ],
)
def test_atmost(n, pred, iterable, expected):
    assert atmost(n, pred, iterable) == expected
