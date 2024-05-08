from dataclasses import dataclass
from datetime import datetime
from functools import reduce
import re
import ipaddress
from typing import Iterable
from Types import MESSAGE_TYPE
import abc


parts = {
    "date": r"(^\S{3})\s*",
    "day": r"(\d+)",
    "time": r"(\d{2}:\d{2}:\d{2})",
    "component": r"(\S{5})",
    "pid": r"sshd\[(\d+)\]:",
    "content": r"(.+)",  # This will match the rest of the line
}

IP_PATTERN = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"


@dataclass
class SSHLog:
    date: str
    day: str
    time: str
    component: str
    pid: str
    content: str

    def __dict__(self):
        return {
            "date": self.date,
            "day": self.day,
            "time": self.time,
            "component": self.component,
            "pid": self.pid,
            "content": self.content,
        }

    def get_time(self):
        current_year = datetime.now().year
        return datetime.strptime(
            f"{current_year} {self.date} {self.day} {self.time}", "%Y %b %d %H:%M:%S"
        )

    def get_content(self):
        return self.content

    def get_ip(self):
        if ip := re.search(IP_PATTERN, self.content):
            return ip.group()


def parse(line: str) -> SSHLog | None:
    search = re.search(
        f"{parts['date']} {parts['day']} {parts['time']} {parts['component']} {parts['pid']} {parts['content']}",
        line,
    )

    if search:
        return SSHLog(
            date=search.group(1),
            day=search.group(2),
            time=search.group(3),
            component=search.group(4),
            pid=search.group(5),
            content=search.group(6),
        )
    return None


def get_ipv4s(log: SSHLog | None) -> Iterable[str]:
    if not log:
        return
    ip = re.search(IP_PATTERN, log.content)
    if ip:
        try:
            ipaddress.ip_address(ip.group())
        except ValueError:
            print(f"Invalid IP: {ip.group()}")
        yield ip.group()


def get_user(log: SSHLog | None) -> str | None:
    if not log:
        return

    user = re.search(r"user (\S+) from", log.content)
    if user:
        return user.group(1)
    else:
        return None


def get_message_type(log: SSHLog) -> MESSAGE_TYPE:
    return reduce(
        lambda acc, msg_type: (
            msg_type if re.match(msg_type.value, log.content) else acc
        ),
        MESSAGE_TYPE,
        MESSAGE_TYPE.UNKNOWN,
    )
