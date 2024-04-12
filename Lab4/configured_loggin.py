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
        super().__init__(name, level)

        # Create handlers
        c_handler = logging.StreamHandler(sys.stdout)
        e_handler = logging.StreamHandler(sys.stderr)

        # Set level for handlers
        c_handler.setLevel(logging.DEBUG)
        e_handler.setLevel(logging.ERROR)

        # Create formatters and add it to handlers
        c_format = logging.Formatter("%(name)s - %(message)s")
        e_format = logging.Formatter("%(name)s - %(message)s")
        c_handler.setFormatter(c_format)
        e_handler.setFormatter(e_format)

        # Add handlers to the logger
        self.addHandler(c_handler)
        self.addHandler(e_handler)

        logging.basicConfig(level=logging.DEBUG)

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
        if self.name in MESSAGE_INFO_TYPE:
            info(f"INFO {id+1}: {self.name}")

        elif self.name in MESSAGE_WARNING_TYPE:
            warning(f"WARNING {id+1}: {self.name}")

        elif self.name in MESSAGE_ERROR_TYPE:
            error(f"ERROR {id+1}: {self.name}")

        elif self.name in MESSAGE_CRITICAL_TYPE:
            critical(f"CRITICAL {id+1}: {self.name}")
