from preproccess_line.preproccess import get_date

import calendar

# log = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'

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


def downloaded_at(day: str, log: str) -> None:
    day, month, year = get_date(log)
    # print(day, month, year)
    is_given_day = True if calendar.day_name[calendar.weekday(
        day=day, month=mapping_month.get(month), year=year)] == day else False

    if is_given_day:
        print(log)
