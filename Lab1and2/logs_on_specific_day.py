from iostream import *


def print_logs_on_specific_day(logs, day: str) -> None:
    """print logs on specific day 

    Args:
        logs (_type_): list of log objects
        day (str): day name
    """
    for log in logs:
        day_name = log.date_.strftime('%A')
        if day_name == day:
            print(log)


if __name__ == '__main__':
    logs = list(read_log())
    # logs = list(read_file())
    params = read_params('Friday')
    print_logs_on_specific_day(logs, day=params[0])
