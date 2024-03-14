from preproccess import get_host
from iostream import *


def get_host_from(domain: str, log: str) -> None:
    if get_host(log).endswith(domain):
        print(log)


if __name__ == '__main__':
    params = read_params('pl')
    read_std(get_host_from, domain=params[0])
