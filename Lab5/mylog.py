import logging
import time
from typing import *


def log(level: logging = logging.INFO):
    def decorator(func_or_class: Callable):
        def wrapper(*args: Any, **kwargs: Any):
            logging.basicConfig(
                filename="Lab5/mylog.log",
                format="%(asctime)s %(levelname)s %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p",
                level=level,
            )
            if callable(func_or_class):
                logging.log(
                    level, "Function {} was called".format(func_or_class.__name__)
                )
                logging.log(level, "Arguments: " + ",".join([str(arg) for arg in args]))
                logging.log(
                    level, "Returned: {}".format(func_or_class(*args, **kwargs))
                )
                start_time = time.time()
                result = func_or_class(*args, **kwargs)
                end_time = time.time()
                logging.log(level, "Function {} ended".format(func_or_class.__name__))
                logging.log(
                    level, "Time taken: {} seconds".format(end_time - start_time)
                )
                return result
            else:
                logging.log(
                    level, "Class {} was instantiated".format(func_or_class.__name__)
                )
                return func_or_class(*args, **kwargs)

        return wrapper

    return decorator


@log(logging.INFO)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


@log(logging.DEBUG)
def compute(*args) -> float:
    return sum(args)


@log(logging.CRITICAL)
def attack():
    print("PALE CI AUTO d-_-b")


if __name__ == "__main__":
    # p = Person("John", 25)
    # print(p)

    compute(1, 2, 3, 4, 5)
    attack()
