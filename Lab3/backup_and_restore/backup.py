import os
from tools import get_src_path, get_backup_path
from JsonWriter import JsonWriter

from BackupInformation import BackupInformation
import subprocess


def create_backup_dir(dest: str) -> None:
    """creates backup directory if it does not exist"""

    if not os.path.exists(dest):
        os.makedirs(dest, exist_ok=True)


def backup(src: str, dest=get_backup_path()) -> bool:
    """creates backup of a file or directory in the specified location with .tar.gz extension

    Args:
        src (str): source path of the file or directory
        dest (str): destination path of the backup file or a directory
    """
    data = BackupInformation(src, "tar.gz")
    create_backup_dir(dest)
    os.chdir(os.path.dirname(src))
    print(f"Backup created: {data.dest_path}")
    subprocess.run(["tar", "-czf", data.dest_path, data.file_name])

    writer = JsonWriter()
    writer.overwrite(data)


def main():
    backup(get_src_path())


if __name__ == "__main__":
    main()
