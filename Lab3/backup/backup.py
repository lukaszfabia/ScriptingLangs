from dataclasses import dataclass
from datetime import datetime
import json
import sys
import subprocess
import os
import pathlib
import re


def get_path_from_line() -> str:
    try:
        path = sys.argv[1]
    except IndexError:
        print("Please provide a path to the file")
        sys.exit(1)
    return path


def create_zip(path: str):
    if not os.path.exists(path) or os.path.isfile(path):
        print("path does not exist or is not a directory")
        sys.exit(1)

    # {timestamp}-{dirname}.{ext}
    def create_name() -> str:
        return f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}-{os.path.basename(path)}.zip'

    name: str = create_name()
    subprocess.run(["zip", "-r", name, path], check=True)
    return str(pathlib.Path().resolve() / name)


def move_backup(path: str, folder_path: str = None):
    if folder_path is None:
        folder_path = os.getenv("BACKUPS_DIR", "/Users/lukaszfabia/.backup")
    folder = pathlib.Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)
    print("Moving backup to: ", folder)
    zip_path = create_zip(path)
    subprocess.run(["cp", zip_path, str(folder)], check=True)
    subprocess.run(["rm", zip_path], check=True)

    _date, _path_to_zip = re.split(
        r"(\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})-(.*).zip", zip_path
    )[1:3]
    update_history(
        BackupInformation(date=_date, copy_path=folder, backup_name=_path_to_zip)
    )


@dataclass(frozen=True)
class BackupInformation:
    date: datetime
    copy_path: pathlib.Path
    backup_name: str

    def __dict__(self):
        return {
            "backup_name": self.backup_name,
            "info:": [
                {"date": self.date},
                {"copy_path": str(self.copy_path)},
            ],
        }


def update_history(info: BackupInformation, file_name: str = "history.json"):
    history_path = pathlib.Path(info.copy_path) / file_name

    if not history_path.exists():
        pathlib.Path(history_path).touch()
        with open(history_path, "w") as file:
            file.write("[]")
    print("Saving history to: ", history_path)
    with open(history_path, "r+") as file:
        try:
            history = json.load(file)
        except json.JSONDecodeError:
            print("Error while reading history file")
            history = []

        history.append(info.__dict__())
        file.seek(0)
        json.dump(history, file, indent=4)
        file.truncate()


def main():
    path = get_path_from_line()
    move_backup(path)


if __name__ == "__main__":
    main()
