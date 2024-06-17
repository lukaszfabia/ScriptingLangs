import random

CHARSET: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
LENGTH: int = 10
COUNT: int = 8


# class PasswordGenerator:

#     def __init__(
#         self, length: int = LENGTH, charset: str = CHARSET, count: int = COUNT
#     ):
#         self._count: int = count
#         self._length: int = length
#         self._charset = charset

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._count == 0:
#             raise StopIteration
#         self._count -= 1
#         return "".join(random.choices(self._charset, k=self._length))


MAX_LENGTH: int = 60
MIN_LENGTH: int = 10


class PasswordGenerator:

    def __init__(
        self,
        max_len: int = MAX_LENGTH,
        min_len: int = MIN_LENGTH,
        charset: str = CHARSET,
        count: int = COUNT,
    ) -> None:
        self._count: int = count
        self.max_len: int = max_len
        self.min_len: int = min_len
        self._charset = charset

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration
        self._count -= 1
        return "".join(
            random.choices(self._charset, k=random.randint(self.min_len, self.max_len))
        )


if __name__ == "__main__":
    ps = PasswordGenerator(min_len=10, max_len=20, count=4, charset=CHARSET)
    for password in ps:
        print(password)
