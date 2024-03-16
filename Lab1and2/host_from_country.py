from iostream import *


def get_host_from(logs, domain: str):
    """prints the logs that have the domain in the host

    Args:
        logs (ParseLog): log objects
        domain (str): domain to search for
    """
    for log in logs:
        if log.host_.endswith(domain):
            print(log)
        else:
            pass


if __name__ == '__main__':
    logs = list(read_log())
    # logs = list(read_file())
    params = read_params('pl')
    get_host_from(logs, domain=params[0])
