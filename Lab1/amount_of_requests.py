from preproccess import *
from iostream import read_std
CODE200: int = 0
CODE302: int = 0
CODE404: int = 0


def update_amount_of_requests(log: str) -> None:
    global CODE200, CODE302, CODE404
    if get_code(log, '200')[0]:
        CODE200 += 1
    elif get_code(log, '302')[0]:
        CODE302 += 1
    elif get_code(log, '404')[0]:
        CODE404 += 1


def get_codes() -> tuple[str, str, str]:
    return f'code 200: {CODE200}\ncode 302: {CODE302}\ncode 404: {CODE404}'


if __name__ == '__main__':
    read_std(update_amount_of_requests)
    print(get_codes())
