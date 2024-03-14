import re
from datetime import time

log = '199.72.81.55 - - [01/Jul/1995:12:34:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'

REGEX_FOR_CODE = r'\[.*\] "(.*)" '

REGEX_FOR_BYTES = r'\[.*\] "(.*)" \d+ (\d+)'

REGEX_FOR_PATH = r'"(?:GET|POST|PUT|DELETE|HEAD|OPTIONS) (\S+) HTTP'

REGEX_FOR_DATE_AND_TIME = r'\[(\d{2}/\w{3}/\d{4}):(\d{2}:\d{2}:\d{2}) -\d{4}\]'

REGEX_FOR_HOST = r'^(\S+)'

DIVDER = 1024 * 1024 * 1024


def parse(log: str, regex: str):
    try:
        match = re.search(pattern=regex, string=log)
        return match.groups() if match else ""
    except AttributeError:
        return ""


def get_code(log: str, code: str) -> tuple[bool, str]:
    parsed = parse(log, f'{REGEX_FOR_CODE}{code}')
    return parsed[0] != "" if parsed else False, code


def gb_sent(log: str) -> float:
    parsed = parse(log, REGEX_FOR_BYTES)
    return float(parsed[1]) / DIVDER if parsed else 0


def get_path(log: str) -> str:
    return parse(log, REGEX_FOR_PATH)[0]


def get_host(log: str) -> str:
    return parse(log, REGEX_FOR_HOST)[0]


def get_date_and_time(log: str) -> tuple[tuple[int, str, int], time]:
    parsed = parse(log, REGEX_FOR_DATE_AND_TIME)

    def get_date_() -> str:
        return int(parsed[0].split(
            '/')[0]), parsed[0].split('/')[1], int(parsed[0].split('/')[2])

    def get_time_() -> str:
        tmp_ = parsed[1].split(':')
        return time(int(tmp_[0]), int(tmp_[1]), int(tmp_[2]))

    return get_date_(), get_time_()


if __name__ == '__main__':
    print(get_code(log, '201'))
    print(gb_sent(log))
    print(get_path(log))
    print(get_host(log))
    print(get_date_and_time(log))
