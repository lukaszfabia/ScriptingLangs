from preproccess import *
from iostream import *


def log_with_code(log: str, code: str) -> None:
    if is_exists(log, code):
        print(log)


if __name__ == '__main__':
    params = read_params('200')
    read_std(func=log_with_code, code=params[0])
