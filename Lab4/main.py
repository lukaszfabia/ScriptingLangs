from pathlib import Path
import sys
from typing import Iterable
import SSHParser
import logging
from configured_loggin import SSHLogger
import typer
import analysis

app = typer.Typer()


def get_logs(
    path: Path = Path("/Users/lukaszfabia/Desktop/ScriptingLangs/Lab4/SSH.log"),
) -> Iterable[str]:
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
    for id, log in enumerate(get_logs()):
        parsed_log = SSHParser.parse(log)
        # logger: SSHLogger = SSHLogger()

        # logger.bytes(log)
        func(
            parsed_log=parsed_log,
            logger=SSHLogger(str(SSHParser.get_message_type(parsed_log).name)),
            id=id,
        )


@app.command()
def users() -> None:
    @iter
    def users_aux(parsed_log: SSHParser.SSHLog | None, **kwargs) -> None:
        if user := SSHParser.get_user_from_log(parsed_log):
            print(user)


@app.command()
def msg() -> None:
    @iter
    def msg_type_aux(
        parsed_log: SSHParser.SSHLog | None, logger: SSHLogger, id: int
    ) -> None:
        print(SSHParser.get_message_type(parsed_log).name)
        logger.log(id)


@app.command()
def ipvs4() -> None:
    @iter
    def ipvs4_aux(parsed_log: SSHParser.SSHLog | None, **kwargs) -> None:
        if ips := SSHParser.get_ipv4s_from_log(parsed_log):
            for ip in ips:
                print(ip)


@app.command()
def rd(n: int = 5) -> None:
    for log in analysis.get_random_log_of_random_user(get_logs(), n):
        print(log)


@app.command()
def time(for_all: bool = False) -> None:
    if not for_all:
        print(analysis.calc_time_for_user(get_logs()))
    else:
        print(analysis.calc_time(get_logs()))


if __name__ == "__main__":
    app()
