import json
from tools import get_backup_path
from pathlib import Path
from BackupInformation import BackupInformation


class JsonWriter:
    def __init__(self, filename: str = "history.json") -> None:
        self.path = Path(get_backup_path()) / filename
        if not self.path.exists():
            self.path.touch()
            with self.path.open("w+") as file:
                json.dump([], file)
        self.filename = filename

    def overwrite(self, data: BackupInformation) -> None:
        """add to history new backup information

        Args:
            data (_type_): _description_
        """

        with open(self.path, "r+") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                print("Error while reading history file")
                history = []

            history.append(data.__dict__())
            file.seek(0)
            json.dump(history, file, indent=4)
            file.truncate()

    def remove(self, data: dict[str, str]) -> None:
        """remove backup information from history

        Args:
            data (_type_): _description_
        """

        with open(self.path, "r+") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                print("Error while reading history file")
                history = []

            history.remove(data)
            file.seek(0)
            json.dump(history, file, indent=4)
            file.truncate()
