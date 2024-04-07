import sys
import subprocess
import os
import pathlib
from enum import Enum
import json


def get_path_from_line() -> str:
    try:
        path = sys.argv[1]
    except IndexError:
        print("Please provide a path to the file")
        sys.exit(1)
    return path


def iterate_file(path: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for file in os.listdir(path):
        result = subprocess.run(
            ["ts-node", "preprocess_file.ts", str(pathlib.Path(path))],
            input=f"{file}\n",
            text=True,
            capture_output=True,
            check=True,
        )
        result = eval(result.stdout)
        results.append(json.loads(json.dumps(result)))

    return results


class KEYS(Enum):
    FILE_PATH = "file path"
    NUMBER_OF_LINES = "number of lines"
    NUMBER_OF_WORDS = "number words"
    NUMBER_OF_CHARACTERS = "number of chars"
    MOST_COMMON_WORD = "most common word"
    MOST_COMMON_CHAR = "most common letter"


class FileStats:
    def __init__(self, list: list[dict[str, str]]):
        self._list = list

    def summarize(self, key: str) -> int:
        return sum([int(item[key]) for item in self._list])

    def most_common(self, key: str) -> tuple[str, int]:
        return max(self._list, key=lambda x: int(x[key][1]))[key]

    def get_read_files(self):
        return sum(1 if item[KEYS.FILE_PATH.value] else 0 for item in self._list)

    def __dict__(self):
        return {
            KEYS.FILE_PATH.value: self.get_read_files(),
            KEYS.NUMBER_OF_LINES.value: self.summarize(KEYS.NUMBER_OF_LINES.value),
            KEYS.NUMBER_OF_WORDS.value: self.summarize(KEYS.NUMBER_OF_WORDS.value),
            KEYS.NUMBER_OF_CHARACTERS.value: self.summarize(
                KEYS.NUMBER_OF_CHARACTERS.value
            ),
            KEYS.MOST_COMMON_WORD.value: self.most_common(KEYS.MOST_COMMON_WORD.value),
            KEYS.MOST_COMMON_CHAR.value: self.most_common(KEYS.MOST_COMMON_CHAR.value),
        }

    def __str__(self) -> str:
        return f"total stats: {json.dumps(self.__dict__(), indent=4)}"


if __name__ == "__main__":
    path = get_path_from_line()
    print(f"Path to the file: {path}")
    lst: list[dict[str, str]] = iterate_file(path)
    stats = FileStats(lst)
    print(stats.__str__())
    # for item in lst:
    #     print(item[KEYS.MOST_COMMON_WORD.value][1])
