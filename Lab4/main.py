from pathlib import Path
import sys
from typing import Iterable
import SSHParser
import logging
from configured_loggin import SSHLogger
import typer
import analysis
from dotenv import load_dotenv
import os

app = typer.Typer()

load_dotenv()

logs_path = os.getenv("PATH_TO_LOGS")


def get_logs(path: Path = Path(logs_path)) -> Iterable[str]:
    """get logs from the directory

    Args:
        path (Path): path to the directory

    Returns:
        list: list of log files
    """
    with open(path, "r") as file:
        for line in file:
            yield line.rstrip()


def iter(func: callable) -> None:
    """iterating over logs

    Args:
        func (callable): function to call on each log
    """
    for id, log in enumerate(get_logs()):
        parsed_log = SSHParser.parse(log)
        # logger: SSHLogger = SSHLogger()

        # logger.bytes(log)
        func(
            parsed_log=parsed_log,
            logger=SSHLogger(str(SSHParser.get_message_type(parsed_log).name)),
            id=id,
            log=log,
        )


@app.command()
def users() -> None:
    """usage: python main.py users - prints all users from logs"""

    @iter
    def users_aux(parsed_log: SSHParser.SSHLog | None, **kwargs) -> None:
        if user := SSHParser.get_user(parsed_log):
            print(user)

    # iter(users_aux)


@app.command()
def msg() -> None:
    """usage python main.py msg - prints message type of the logs"""

    @iter
    def msg_type_aux(
        parsed_log: SSHParser.SSHLog | None, logger: SSHLogger, id: int, **kwargs
    ) -> None:
        # print(SSHParser.get_message_type(parsed_log).name)
        logger.log(id)


@app.command()
def ipvs4() -> None:
    """usage: python main.py ipvs4 - prints all ipv4 addresses from logs"""

    @iter
    def ipvs4_aux(parsed_log: SSHParser.SSHLog | None, **kwargs) -> None:
        if ips := SSHParser.get_ipv4s(parsed_log):
            for ip in ips:
                print(ip)


@app.command()
def rd(n: int = 5) -> None:
    """usage: python main.py rd ?--n=%d - prints n random logs from random user

    Args:
        n (int, optional): number of entries. Defaults to 5.
    """
    for id, log in enumerate(analysis.get_random_log_of_random_user(get_logs(), n)):
        logger: SSHLogger = SSHLogger(str(SSHParser.get_message_type(log).name))
        # print(log)
        logger.log(id)


@app.command()
def time(for_all: bool = False) -> None:
    """usage: python main.py time ?--for_all - prints time for all users
    Args:
        for_all (bool, optional): take overall time.
    """
    if not for_all:
        print(analysis.calc_time_for_user(get_logs()))
    else:
        print(analysis.calc_time(get_logs()))


@app.command()
def main() -> None:
    """usage: python main.py main"""

    @iter
    def aux(parsed_log: SSHParser.SSHLog | None, logger: SSHLogger, id: int, log: str):
        logger.bytes(log)
        logger.log(id)


if __name__ == "__main__":
    app()
