import random

CHARSET: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
LENGTH: int = 10
COUNT: int = 8


class PasswordGenerator:

    def __init__(
        self, length: int = LENGTH, charset: str = CHARSET, count: int = COUNT
    ):
        self._count: int = count
        self._length: int = length
        self._charset = charset

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration
        self._count -= 1
        return "".join(random.choices(self._charset, k=self._length))


if __name__ == "__main__":
    pg = PasswordGenerator(length=12, count=5)
    for password in pg:
        print(password)
