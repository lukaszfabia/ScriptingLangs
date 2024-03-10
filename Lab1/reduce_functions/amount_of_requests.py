from preproccess_line.preproccess import *
CODE200: int = 0
CODE302: int = 0
CODE404: int = 0


def update_amount_of_requests(request: str) -> None:
    global CODE200, CODE302, CODE404
    if is_exists(request, '200'):
        CODE200 += 1
    elif is_exists(request, '302'):
        CODE302 += 1
    elif is_exists(request, '404'):
        CODE404 += 1


def getAmountOfRequests200() -> int:
    return CODE200


def getAmountOfRequests302() -> int:
    return CODE302


def getAmountOfRequests404() -> int:
    return CODE404
