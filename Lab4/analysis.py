from dataclasses import dataclass
from datetime import datetime, timedelta
import random
from typing import Dict, Iterable, List, Tuple
import numpy as np

from main import get_logs
import SSHParser


def convert(date: str) -> float:
    """convert date to seconds

    Args:
        date (str): data as a string in %H:%M:%S format

    Returns:
        timedelta: seconds
    """
    _date: datetime = datetime.strptime(date, "%H:%M:%S")
    return timedelta(
        hours=_date.hour, minutes=_date.minute, seconds=_date.second
    ).total_seconds()


def calc_time(logs: Iterable[str], is_parsed: bool = False) -> Tuple[str, str]:
    """calculates mean time and stad. deviadtion of spent time

    Args:
        logs (Iterable[str]): represents line with log

    Returns:
        Tuple[str, str]: result converted to normal time
    """
    if not is_parsed:
        arr = [convert(SSHParser.parse(log).time) for log in logs]
    else:
        arr = logs
    reconvert = lambda sec: str(timedelta(seconds=sec))
    return reconvert(np.mean(arr)), reconvert(np.std(arr))


def calc_time_for_user(logs: Iterable[str]) -> Dict[str, Tuple[str, str]]:
    """calucates avrage and std dev of a time

    Args:
        logs (Iterable[str]): lane with log

    Returns:
        Dict[str, Tuple[str, str]]: user: "mean", "std_dev"
    """
    user_and_time: Dict[str, List[int]] = {}
    for log in logs:
        parsed_log: SSHParser.SSHLog | None = SSHParser.parse(log)
        user: str | None = SSHParser.get_user(parsed_log)
        if parsed_log and user:
            if user in user_and_time:
                user_and_time[user].append(convert(parsed_log.time))
            else:
                user_and_time[user] = [convert(parsed_log.time)]

    return update_user_time(user_and_time)


def update_user_time(user_and_time: Dict[str, List[int]]) -> Dict[str, Tuple[str, str]]:
    """update user time by setting mean and std. deviation

    Args:
        user_and_time (Dict[str, List[int]]): username and his spent time in seconds

    Returns:
        Dict[Tuple[str, str]]: username and his mean and std. deviation in normal time
    """
    users_time: Dict[str, Tuple[str, str]] = {}
    for username, time in user_and_time.items():
        if time:
            users_time[username] = calc_time(time, is_parsed=True)
    return users_time


# for user, time in calc_time_for_user(get_logs()).items():
#     print(user, time)


def get_random_log_of_random_user(logs: Iterable[str], n: int) -> List[str]:
    """Get n random logs of random user

    Args:
        logs (Iterable[str]): Collection of logs
        n (int): Number of logs to retrieve
    Returns:
        List[str]: List of random logs
    """
    parsed_logs: List[SSHParser.SSHLog] = [SSHParser.parse(log) for log in logs]

    random_user: str = None

    # getting random user
    while random_user is None:
        random_user = SSHParser.get_user(
            parsed_logs[random.randint(0, len(parsed_logs) - 1)]
        )

    print(f"Random user: {random_user}")
    user_logs = [log for log in parsed_logs if SSHParser.get_user(log) == random_user]
    return random.sample(user_logs, min(n, len(user_logs)))


@dataclass(frozen=True)
class UsersActivity:
    """represents user activity"""

    username: str
    activity: int

    def __str__(self) -> str:
        return f"{self.username}: {self.activity}"


def get_stats_for_user(
    logs: Iterable[str], see_all: bool = False
) -> List[UsersActivity]:
    """Get statistics for all users

    Args:
        logs (Iterable[str]): raw logs
        see_all (bool, optional): all users activity. Defaults to False.

    Returns:
        List[UsersActivity]: list with users activity
    """
    activity: Dict[str, int] = {}
    for log in logs:
        parsed_log: SSHParser.SSHLog | None = SSHParser.parse(log)
        user: str | None = SSHParser.get_user(parsed_log)
        if user:
            if user in activity:
                activity[user] += 1
            else:
                activity[user] = 1

    sorted_activity = sorted(activity.items(), key=lambda x: x[1], reverse=True)
    if see_all:
        return [UsersActivity(user, act).__str__() for user, act in sorted_activity]
    else:
        return [
            UsersActivity(sorted_activity[0][0], sorted_activity[0][1]).__str__(),
            UsersActivity(sorted_activity[-1][0], sorted_activity[-1][1]).__str__(),
        ]
