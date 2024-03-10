import os
PATH = f'{os.getcwd()}\\Lab1\\NASA.txt'


def read(name=PATH) -> None:
    with open(name, 'r') as file:
        data = file.readline()
        while data:
            data = file.readline()
            print(data)
