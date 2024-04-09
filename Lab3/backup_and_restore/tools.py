import sys
import os
from pathlib import Path


def get_src_path() -> str:
    """get source path from the command line arguments to make a backup

    Returns:
        str: source path
    """
    try:
        path = sys.argv[1]
    except IndexError:
        print("Default path is used: ", get_backup_path())
        return get_backup_path()  # for restore
    return path


def get_backup_path() -> str:
    """backup directory path

    Returns:
        str: path to the backup directory or default env path
    """
    backup_dir = os.environ.get(
        "BACKUPS_DIR", os.path.join(os.path.expanduser("~"), ".backup")
    )
    return backup_dir
