from iostream import *

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


def get_failed_reads(logs, is_merged=False) -> list | tuple[list, list]:
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


def log_to_dict(logs: list) -> dict:
    return dict(map(lambda log: (log, log.__dict__()), logs))


def get_addrs(logs: dict):
    for log in logs.keys():
        yield log


def summarize_logs(logs: dict):
    """prints the dates of the logs for each host
        model of the dictionary:
        {
            'host1': {
                'amount of requests': int, 
                'fist request': datetime,
                'last request': datetime
            },
            'host2': {
                ...
            }, 
            'ratio' : float # amount of requests with code / total amount of requests
        }
    Args:
        logs (dict): logs as dictionary
    """
    data = {
        'ratio': 0
    }

    for key, value in logs.items():
        if key.host_ in data:
            data.update({key.host_: {
                'amount of requests': data[key.host_].get('amount of requests', 0) + 1,
                'last request': value['date'],
                'first request': data[key.host_]['first request']
            }})
        else:
            data.update({key.host_: {
                'amount of requests': 1,
                'first request': value['date'],
                'last request': value['date']
            }})

        if value['code'] == 200:
            data['ratio'] = data.get('ratio', 0) + 1
    data['ratio'] = round(data['ratio'] / len(logs), 2)

    return data


def print_dict_entry_dates(data: dict):
    for host, log in data.items():
        if host != 'ratio':
            print(f'\n\n{host}:\n\n\tamount of requests: {
                  log["amount of requests"]}')
            print(f'\tfirst request: {log["first request"]}')
            print(f'\tlast request: {log["last request"]}')
    print(f'\nratio: {data["ratio"]}')


if __name__ == '__main__':
    lst = list(read_file('NASA.txt'))
    # sorted_lst = sort_log(lst, key=lambda log: log.bytes_)
    # for curr in sorted_lst:
    #     print(curr)
    for elem in get_entries_by_addr(lst, '199.120.110.21'):
        print(elem)
    # print()
    # print_entries(lst)
    # lst = list(read_file('tmp.txt'))
    # dic = log_to_dict(lst)
    # keys = get_addrs(dic)
    # print_dict_entry_dates(summarize_logs(dic))
    # for elem in get_entries_by_extension(lst, '.gif'):
    #     print(elem)
