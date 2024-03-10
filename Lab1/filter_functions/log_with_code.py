from preproccess_line.preproccess import *


def log_with_code(code: str, log: str) -> None:
    if is_exists(log, code):
        print(log)
