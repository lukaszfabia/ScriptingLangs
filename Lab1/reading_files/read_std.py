from reduce_functions.amount_of_requests import *
from reduce_functions.sent_data import *
from reduce_functions.max_resource import *
from reduce_functions.graphic_downloads import *

from filter_functions.log_with_code import *
from filter_functions.resources_downloaded import *
from filter_functions.downloaded_in_day import *
from filter_functions.host_from_given_country import *


def read_std() -> str:
    # data = ""
    while True:
        try:
            line: str = input()
            run_algorithms(line)
        except EOFError:
            break


def run_algorithms(line: str) -> None:
    reduce_algorithms(line)
    filter_algorithms(line)


def reduce_algorithms(line: str) -> None:
    update_amount_of_requests(line)
    update_amount_of_sent_data(line)
    update_max_resource(line)
    update_graphic_downloads(line)


def filter_algorithms(line: str) -> None:
    # # print('Log with code 200: ')
    # log_with_code('200', line)

    # # print('Resources downloaded between 22 and 6 hour: ')
    # resources_downloaded_between(start='22', end='6', log=line)

    # # print('Resources downloaded in day: ')
    # downloaded_at('Friday', line)

    get_host_from('pl', line)
