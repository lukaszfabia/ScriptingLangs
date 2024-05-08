from typing import *

import pytest

T = TypeVar("T")


def forall(pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    match iterable:
        case []:
            return True
        case [head, *tail]:
            return pred(head) and forall(pred, tail)


def exists(pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    match iterable:
        case []:
            return False
        case [head, *tail]:
            return pred(head) or exists(pred, tail)


def atleast(n: int, pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    return sum(1 for elem in iterable if pred(elem)) >= n


def atmost(n: int, pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    return sum(1 for elem in iterable if pred(elem)) <= n
