from iostream import *


def log_with_code(logs, code: int) -> None:
    """prints log with given code

    Args:
        logs (ParseLog): log objects
        code (int): status code
    """
    for log in logs:
        if int(log.code_) == code:
            print(log)


if __name__ == '__main__':
    # logs = list(read_log())
    logs = list(read_file())
    params = read_params(200)
    log_with_code(logs, code=params[0])
