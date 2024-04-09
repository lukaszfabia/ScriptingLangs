from datetime import datetime
import os
from pathlib import Path
from typing import override
from tools import get_backup_path, get_src_path


class BackupInformation:

    def __init__(self, src_path, ext: str):
        self.src_path: Path = Path(src_path).resolve()
        self.date: datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.ext: str = ext
        self.file_name = self.src_path.name
        self.dest_path = (
            Path(get_backup_path()) / f"{self.date}_{self.file_name}.{self.ext}"
        ).resolve()

    def __str__(self):
        return f"{self.date}_{self.file_name}.{self.ext}"

    def __dict__(self):
        return {
            "file_name": self.file_name,
            "info": [
                {"src_path": str(self.src_path)},
                {"date": self.date},
            ],
        }
