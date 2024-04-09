import json
import os
import shutil
import subprocess
from tools import get_src_path, get_backup_path
from BackupInformation import BackupInformation
from pathlib import Path
from JsonWriter import JsonWriter


def restore(dest: str, backup_file: BackupInformation) -> None:
    """unpack the backup file to the destination

    Args:
        dest (str): destination path
        backup_file (BackupInformation): backup object to unpack
    """
    file_to_unpack = Path(get_backup_path()) / f'{backup_file["info"][1]["date"]}_{backup_file["file_name"]}.tar.gz'
    # for filename in os.listdir(dest):
    #     file_path = os.path.join(dest, filename)
    #     if os.path.isfile(file_path) or os.path.islink(file_path):
    #         os.unlink(file_path)
    #     elif os.path.isdir(file_path):
    #         shutil.rmtree(file_path)

    subprocess.run(["tar", "-xzf", file_to_unpack, "-C", dest])
    print(f"Unpacked file in: {file_to_unpack} to {dest}")


def remove_tar_file(dest: str) -> None:
    """optional remove of the backup file

    Args:
        dest (str): path to the backup file
    """
    subprocess.run(["rm", "-r", dest])

def get_dest() -> str:
    """path to unpack the backup

    Returns:
        str: destination path
    """
    return get_src_path()


def get_backups(history_file_name: str = "history.json") -> list[dict[str, str]]:
    """get backups from history file

    Args:
        history_file_name (str, optional): _description_. Defaults to "history.json".

    Returns:
        list[dict[str, str]]: jsonified backups
    """
    print(os.path.join(get_backup_path(), history_file_name))
    with open(os.path.join(get_backup_path(), history_file_name), "r") as f:
        history = json.load(f)

    return history


def get_data_from_user(history: list[dict[str, str]]) -> tuple[dict[str, str]]:
    """users input to choose the backup to restore

    Args:
        history (list[dict[str, str]]): all backups

    Returns:
        tuple[dict[str, str], int]: choosen backup
    """
    for index, record in enumerate(reversed(history)):
        print(f"{index}: {record["info"][1]['date']} - {record['file_name']}")

    picked: int = -1
    while picked < 0 or picked > len(history):
        picked = int(input("Enter the number of the backup to restore: "))

    return history[index]


def main():
    backups = get_backups()
    # print(backups)
    data_to_unpack = get_data_from_user(backups)
    
    # update history
    writer = JsonWriter()
    writer.remove(data_to_unpack)
    
    restore(get_dest(), data_to_unpack)
    
    name = data_to_unpack["file_name"]
    wanna_remove_backup = input(f"Do you want to remove the backup {name}.tar.gz? [y/n]: ")
    if wanna_remove_backup.lower() in ("y", "yes"):
        remove_tar_file(Path(get_backup_path()) / f'{data_to_unpack["info"][1]["date"]}_{data_to_unpack["file_name"]}.tar.gz')


if __name__ == "__main__":
    main()
