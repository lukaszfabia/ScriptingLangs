
import re
log = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'

REGEX_FOR_CODE = r'\[.*\] "(.*)" '

REGEX_FOR_BYTES = r'\[.*\] "(.*)" \d+ (\d+)'

REGEX_FOR_PATH = r'"(?:GET|POST|PUT|DELETE|HEAD|OPTIONS) (\S+) HTTP'

# te dwa mozna w jedno poloczyc

REGEX_FOR_HOUR = r'\[\d{2}/\w{3}/\d{4}:(\d{2}:\d{2}:\d{2}) -\d{4}\]'

REGEX_FOR_DATE = r'\[(\d{2}/\w{3}/\d{4}):\d{2}:\d{2}:\d{2} -\d{4}\]'

DIVDER = 10000000


def is_exists(log: str, code: str) -> str:
    try:
        match = re.search(with_code(code), log)
        return True if match.group(0) else False
    except AttributeError:
        return False


def with_code(code: str) -> str:
    return REGEX_FOR_CODE + code


def gb_sent(log: str) -> float:
    try:
        match = re.search(REGEX_FOR_BYTES, log)
        return float(match.group(2)) / DIVDER

    except AttributeError:
        return 0


def get_path(log: str) -> str:
    try:
        path = re.search(REGEX_FOR_PATH, log)
        return path.group(1)
    except AttributeError:
        return ""


def get_hour(log: str) -> int:
    try:
        hour = re.search(REGEX_FOR_HOUR, log)
        return int(hour.group(1).split(':')[0])
    except AttributeError:
        return ""


def get_date(log: str) -> tuple[int, str, int]:
    """gets date from log

    Args:
        log (str): like this '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'

    Returns:
        tuple[str, str, str]: date splitted by '/' like this ('01', 'Jul', '1995')
        * day as int 
        * month as str
        * year as int
    """
    try:
        date = re.search(REGEX_FOR_DATE, log)
        return int(date.group(1).split('/')[0]), date.group(1).split('/')[1], int(date.group(1).split('/')[2])
    except AttributeError:
        return ""


def get_host(log: str) -> str:
    try:
        host = re.search(r'^(\S+)', log)

        return host.group(1)
    except AttributeError:
        return ""
