import re
from datetime import datetime

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


class ParseLog:

    def __init__(self, log: str) -> None:
        self.regex_ = r'^(\S+) - - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) ([+\-]\d{4})\] "(GET|POST|PUT|DELETE|HEAD|OPTIONS) (\S+) HTTP/1\.\d" (\d+) (\d+)'
        self.log_: str = log
        self.host_: str = None
        self.date_: datetime = None
        self.method_: str = None
        self.path_: str = None
        self.code_: int = None
        self.bytes_: str = None

    def parse_date(self, date: str) -> datetime:
        date_ = re.split(r'[/:]', date)
        date_ = [int(curr) if curr!='Jul' else int(mapping_month.get(curr)) for curr in date_]
        return datetime(day=date_[0], month=date_[1], year=date_[2], hour=date_[3], minute=date_[4], second=date_[5])
    
    def set_data(self, parsed_log: re.Match[str])-> None:
        self.host_ = parsed_log.group(1)
        self.date_ = self.parse_date(parsed_log.group(2))
        self.method_ = parsed_log.group(4)
        self.path_ = parsed_log.group(5)
        self.code_ = parsed_log.group(6)
        self.bytes_ = parsed_log.group(7)

    def wrap_log(self) -> tuple:
        match_ = re.search(string=self.log_, pattern=self.regex_)
        if match_:
            self.set_data(match_)
            return (self.host_, self.date_, self.method_, self.path_, self.code_, self.bytes_)