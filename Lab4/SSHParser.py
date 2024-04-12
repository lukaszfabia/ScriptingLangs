from dataclasses import dataclass
from functools import reduce
import re
import ipaddress
from typing import Iterable
from Types import MESSAGE_TYPE


parts = {
    "date": r"(^\S{3})\s*",
    "day": r"(\d+)",
    "time": r"(\d{2}:\d{2}:\d{2})",
    "component": r"(\S{5})",
    "pid": r"sshd\[(\d+)\]:",
    "content": r"(.+)",  # This will match the rest of the line
}


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


def get_ipv4s_from_log(log: SSHLog | None) -> Iterable[str]:
    if not log:
        return
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log.content)
    if ip:
        try:
            ipaddress.ip_address(ip.group())
        except ValueError:
            print(f"Invalid IP: {ip.group()}")
        yield ip.group()


def get_user_from_log(log: SSHLog | None) -> str | None:
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