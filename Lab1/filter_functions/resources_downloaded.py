from preproccess_line.preproccess import get_hour
# 22 - 6


def resources_downloaded_between(start: int, end: int, log: str) -> None:
    hour = get_hour(log)
    # jakis dziwny bug z typowaniem
    end = int(end)
    start = int(start)
    if start > end:
        if not end < hour and hour < start:
            print(log)
    else:
        if end < hour and hour < start:
            print(log)
