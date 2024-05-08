from typing import *


def make_generator(pred: Callable):
    def aux():
        i: int = 1
        while True:
            yield pred(i)
            i += 1

    return aux


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    gen = make_generator(lambda x: x**2)
    for i, val in enumerate(gen()):
        print(val, end=", ")
        if i == 10:
            break

    print("\nSeq square, Done! ")

    gen = make_generator(fib)
    for i, val in enumerate(gen()):
        print(val, end=", ")
        if i == 10:
            break

    print("\nFibonacci, Done! ")
