from iostream import read_std
from preproccess import gb_sent, get_path
from present_data import print_output

MAX_RESOURCE: int = 0
PATH: str = ""


def update_max_resource(log: str):
    global MAX_RESOURCE, PATH
    if MAX_RESOURCE < gb_sent(log):
        MAX_RESOURCE = gb_sent(log)
        PATH = get_path(log)
    pass


def get_max_resource_and_path() -> tuple[int, str]:
    return MAX_RESOURCE, PATH


if __name__ == '__main__':
    read_std(update_max_resource)
    print_output(max_resource=f'{get_max_resource_and_path()}')
