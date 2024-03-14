from preproccess import get_date_and_time
from iostream import *
import calendar

mapping_month = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}


def print_logs_on_specific_day(log: str, day: str) -> None:
    day_, month_, year_ = get_date_and_time(log)[0]
    is_given_day = True if calendar.day_name[calendar.weekday(
        day=day_, month=mapping_month.get(month_), year=year_)] == day else False

    if is_given_day:
        print(log)


if __name__ == '__main__':
    params = read_params('Friday')

    read_std(print_logs_on_specific_day, day=params[0])
