from preproccess import *
from iostream import read_std
CODE200: int = 0
CODE302: int = 0
CODE404: int = 0


def update_amount_of_requests(log: str) -> None:
    global CODE200, CODE302, CODE404
    if is_exists(log, '200'):
        CODE200 += 1
    elif is_exists(log, '302'):
        CODE302 += 1
    elif is_exists(log, '404'):
        CODE404 += 1


def get_codes() -> tuple[str, str, str]:
    return f'code 200: {CODE200}\ncode 302: {CODE302}\ncode 404: {CODE404}'


if __name__ == '__main__':
    read_std(update_amount_of_requests)
    print(get_codes())
