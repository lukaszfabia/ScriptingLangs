import sys
from Parser import ParseLog
from operator import itemgetter


def read_log():
    # lst = []
    i = 0
    for line in sys.stdin:
        curr = ParseLog(line.rstrip())
        # if curr.bytes_ is None or curr.code_ is None:
        # print(f'{i}. {curr}')
        print(curr)
        i += 1
        yield curr

        # lst.append(ParseLog(line.rstrip()))

    # return lst


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
    # def condition(log: str) -> bool: return log[0] == addr
    # return list(filter(lambda log: condition(log), logs))
    lst = []

    for log in logs:
        try:
            if log[0] == addr or log[0].endswith(addr):
                lst.append(log)
        except TypeError:
            pass

    for log in lst:
        print(log)
    # return lst


def get_entries_by_code(logs, code: str):
    # def condition(log: str) -> bool: return log[0] == addr
    # return list(filter(lambda log: condition(log), logs))
    lst = []

    for log in logs:
        try:
            if log[4] == code:
                lst.append(log)
        except TypeError:
            pass

    for log in lst:
        print(log)
    # return lst


def get_failed_reads():
    pass


def get_entries_by_extension():
    pass


def print_entries(lst):
    for entry in lst:
        print(entry)


if __name__ == '__main__':
    lst = list(read_log())
    # sorted_lst = sort_log(lst, key=lambda log: log.bytes_)
    # for curr in sorted_lst:
    #     print(curr)
    # print(get_entries_by_addr(lst, 'pl'))
    # print()
    # print_entries(lst)
