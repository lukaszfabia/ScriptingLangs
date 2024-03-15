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

log = 'ix-sd11-26.ix.netcom.com - - [01/Jul/1995:00:05:06 -0400] "GET /cgi-bin/imagemap/countdown?107,144 HTTP/1.0" 302 3243296'
log1 = 'ix-sd11-26.ix.netcom.com - - [01/Jul/1995:00:05:06 -0400] "GET / HTTP/1.0" 302 -'
log2 = 'firewall.dfw.ibm.com - - [20/Jul/1995:07:53:24 -0400] "1/history/apollo/images/" 400 -'

REGEX = r'^(\S+) - - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) ([+\-]\d{4})\] "(\S+).*? (\S+).*?" (\d{3}) (\S+)'


class ParseLog:

    def __init__(self, log: str) -> None:
        self.regex_ = REGEX
        self.log_: str = log
        self.host_: str = None
        self.date_: datetime = None
        self.method_: str = None
        self.path_: str = None
        self.code_: int = None
        self.bytes_: int = None
        self.matched = self.wrap_log()

    def parse_date(self, date: str) -> datetime:
        date_ = re.split(r'[/:]', date)
        date_ = [int(curr) if curr != 'Jul' else int(
            mapping_month.get(curr)) for curr in date_]
        return datetime(day=date_[0], month=date_[1], year=date_[2], hour=date_[3], minute=date_[4], second=date_[5])

    def set_data(self, parsed_log: re.Match[str]) -> None:
        self.host_ = parsed_log.group(1)
        self.date_ = self.parse_date(parsed_log.group(2))
        self.method_ = str(parsed_log.group(4)).upper()
        self.path_ = parsed_log.group(5)
        self.code_ = int(parsed_log.group(6))
        self.bytes_ = int(parsed_log.group(
            7)) if parsed_log.group(7) != '-' else 0

    def wrap_log(self) -> bool:
        match_ = re.search(string=self.log_, pattern=self.regex_)
        if match_:
            self.set_data(match_)
            return True
        else:
            return False

    def __repr__(self) -> str:
        return repr((self.host_, self.date_, self.method_, self.path_, self.code_, self.bytes_))
