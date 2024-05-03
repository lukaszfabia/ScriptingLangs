import logging
import sys
from logging import Logger, info, debug, warning, error, critical
from typing import override

from Types import (
    MESSAGE_INFO_TYPE,
    MESSAGE_WARNING_TYPE,
    MESSAGE_ERROR_TYPE,
    MESSAGE_CRITICAL_TYPE,
)


class SSHLogger(Logger):
    def __init__(self, name: str, level: int | str = 0) -> None:
        """
        Initialize the SSHLogger with a name and level.

        Args:
            name (str): general name of the content log
            level (int | str): The level of the logger. Default is 0.
        """
        super().__init__(name, level)

        debug_handler = logging.StreamHandler(sys.stdout)
        error_handler = logging.StreamHandler(sys.stderr)
        info_handler = logging.StreamHandler(sys.stdout)
        warning_handler = logging.StreamHandler(sys.stdout)
        critical_handler = logging.StreamHandler(sys.stderr)

        debug_handler.setLevel(logging.DEBUG)
        error_handler.setLevel(logging.ERROR)
        info_handler.setLevel(logging.INFO)
        warning_handler.setLevel(logging.WARNING)
        critical_handler.setLevel(logging.CRITICAL)

        formatter = logging.Formatter("%(name)s - %(message)s")
        c_format = formatter
        e_format = formatter

        debug_handler.setFormatter(c_format)
        error_handler.setFormatter(e_format)

    def bytes(self, log: str) -> int:
        """logging the bytes of the every lane(log)

        Args:
            log (str): represents lane

        Returns:
            int: bytes of the lane
        """
        bytes: int = len(log.encode("utf-8"))
        debug(f"Read bytes: {bytes}")
        return bytes

    def log(self, id: str) -> None:
        """logging the message with the id

        Args:
            id (str): represents the id of the message
        """
        if self.name in MESSAGE_INFO_TYPE:
            self.info(f"INFO {id+1}: {self.name}")

        elif self.name in MESSAGE_WARNING_TYPE:
            self.warning(f"WARNING {id+1}: {self.name}")

        elif self.name in MESSAGE_ERROR_TYPE:
            self.error(f"ERROR {id+1}: {self.name}")

        elif self.name in MESSAGE_CRITICAL_TYPE:
            self.critical(f"CRITICAL {id+1}: {self.name}")
