from dataclasses import dataclass
from typing import *
from datetime import datetime, timedelta
from SSHParser import SSHLog, MESSAGE_TYPE, parse, get_message_type, get_ipv4s, get_user


@dataclass
class Attack:
    ip: str
    user: Optional[str]
    first_time: datetime
    last_time: datetime
    number_of_attempts: int

    def __str__(self) -> str:
        return f"Attack by {self.user} from {self.ip} with {self.number_of_attempts} attempts from {self.first_time} to {self.last_time}"


def failed(log: SSHLog) -> bool:
    return get_message_type(log) in (
        MESSAGE_TYPE.FAILED_PASSWORD,
        MESSAGE_TYPE.REPEATED_MESSAGE,
        MESSAGE_TYPE.FAILED_NONE,
        MESSAGE_TYPE.INVALID_USER,
        MESSAGE_TYPE.INVALID_USER_FROM,
    )


def update_attempts_and_attacks(
    attempts: Dict[Tuple[str, Optional[str]], List[datetime]],
    attacks: List[Attack],
    ip: str,
    user: Optional[str],
    timestamp: datetime,
    interval_sec: int,
) -> None:
    key = (ip, user)
    if key not in attempts:
        attempts[key] = []

    attempts[key] = [
        time
        for time in attempts[key]
        if timestamp - time <= timedelta(seconds=interval_sec)
    ]

    attempts[key].append(timestamp)

    # dodajemy gdy bylo 6 failed
    if len(attempts[key]) >= 6:
        first_attempt = min(attempts[key])
        last_attempt = max(attempts[key])
        attacks.append(
            Attack(
                ip=ip,
                user=user,
                first_time=first_attempt,
                last_time=last_attempt,
                number_of_attempts=len(attempts[key]),
            )
        )


def detect_attack(
    raw_logs: Iterable[str], interval_sec: int, single: bool
) -> List[Attack]:
    """Detect brute force attacks.

    This function takes in a collection of raw logs and detects brute force attacks based on the provided parameters.

    Args:
        raw_logs (Iterable[str]): A collection of log lines to parse.
        interval_sec (int, optional): The time range in seconds to consider for detecting attacks. Defaults to 30.
        single (bool, optional): Indicates whether the detection is for a single user or all users. Defaults to True.

    Returns:
        List[Attack]: A list of detected attacks for the given user(s).

    """
    attempts: Dict[Tuple[str, Optional[str]], List[datetime]] = {}
    attacks: List[Attack] = []

    for log in raw_logs:
        log = parse(log)
        # bierzemy tylko failed
        if failed(log):
            ips = get_ipv4s(log)
            user = get_user(log) if single else None
            timestamp = log.get_time()
            # lecimy po logach
            for ip in ips:
                update_attempts_and_attacks(
                    attempts, attacks, ip, user, timestamp, interval_sec
                )

    return attacks
