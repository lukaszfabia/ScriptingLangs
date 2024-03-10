import os
PATH = f'{os.getcwd()}\\Lab1\\NASA.txt'


def is_empty(string: str) -> bool:
    return string == ''


def read_std() -> str:
    data = ""
    while True:
        line: str = input()
        print(line)
        data += line
        if is_empty(line) or line == 'EOF':
            return data



def read(name: str) -> None:
    with open(name, 'r') as file:
        data = file.readline()
        while data:
            data = file.readline()
            print(data)


if __name__ == '__main__':
    read_std()
