from preproccess_line.preproccess import get_host


def get_host_from(domain: str, log: str) -> None:
    if get_host(log).endswith(domain):
        print(log)
