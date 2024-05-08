from functools import lru_cache
from make_generator import make_generator
from typing import Callable


@lru_cache()
def mem_gen(pred: Callable):
    def memoized(x):
        return pred(x)

    return make_generator(memoized)


if __name__ == "__main__":
    gen = mem_gen(lambda x: x**2 + 1)
    for i, val in enumerate(gen()):
        print(val, end=", ")
        if i == 10:
            break

    print("\nSeq, Done! ")
