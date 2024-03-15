from iostream import *


def reduce_requests(logs) -> str:
    """summarize the amount of requests with different status codes

    Args:
        logs (ParseLog): log objects

    Returns:
        str: result of summarizing 
    """
    code200 = code302 = code404 = 0
    for log in logs:
        match int(log.code_):
            case 200:
                code200 += 1
            case 302:
                code302 += 1
            case 404:
                code404 += 1
            case _:
                pass
    return f'code 200: {code200}\ncode 302: {code302}\ncode 404: {code404}'


if __name__ == '__main__':
    logs = list(read_log())
    # logs = list(read_file())
    print(reduce_requests(logs))
