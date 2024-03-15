from iostream import *
from logs_on_specific_day import print_logs_on_specific_day
from max_bytes import get_max_bytes

# 691502 klothos.crl.research.digital.com - - [10/Jul/1995:16:45:50 -0400] "♣☺" 400 -
# 1421674 firewall.dfw.ibm.com - - [20/Jul/1995:07:34:34 -0400] "1/history/apollo/images/" 400 -
# 1422423 firewall.dfw.ibm.com - - [20/Jul/1995:07:53:24 -0400] "1/history/apollo/images/" 400 -
# 1454419 128.159.122.20 - - [20/Jul/1995:15:28:50 -0400] "k��♥tx��♦tG��t̓�" 400 -
# 1649963 128.159.122.20 - - [24/Jul/1995:13:52:50 -0400] "k��♥tx��♦tG��t̓�" 400 -


def sort_log(logs, key=None):
    def aux(logs):
        if key:
            return sorted(logs, key=key)
        else:
            return sorted(logs, key=lambda log: log.bytes_)

    try:
        return aux(logs)
    except TypeError:
        print('Error: Invalid key')


def get_entries_by_addr(logs, addr: str):
    for log in logs:
        if log.host_ == addr:
            yield log


def get_entries_by_code(logs, code: str):
    for log in logs:
        if log.code_ == code:
            yield log


def get_failed_reads(logs, is_merged=True) -> list | tuple[list, list]:
    failed_logs = []
    lst4xx = []
    lst5xx = []

    for log in logs:
        if str(log.code_).startswith('4'):
            lst4xx.append(log)
        elif str(log.code_).startswith('5'):
            lst5xx.append(log)

    if is_merged:
        failed_logs = lst4xx + lst5xx
    else:
        failed_logs = lst4xx, lst5xx

    return failed_logs


def get_entries_by_extension(logs, extension: str):
    return filter(lambda log: log.path_.endswith(extension), logs)


def print_entries(lst):
    for entry in lst:
        print(entry)


def print_logs_on_specific_day(logs, day='Friday') -> None:
    for log in logs:
        # Pobieramy nazwę dnia tygodnia z obiektu datetime
        day_name = log.date_.strftime('%A')
        if day_name == day:
            print(log)


if __name__ == '__main__':
    # lst = list(read_log())
    # sorted_lst = sort_log(lst, key=lambda log: log.bytes_)
    # for curr in sorted_lst:
    #     print(curr)
    # print(get_entries_by_addr(lst, 'pl'))
    # print()
    # print_entries(lst)
    lst = list(read_file())
    for elem in get_failed_reads(lst, False):
        print(f'{elem[0]}\n{elem[1]}')
    # for elem in get_entries_by_extension(lst, '.gif'):
    #     print(elem)
