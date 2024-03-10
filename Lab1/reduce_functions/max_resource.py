from preproccess_line.preproccess import gb_sent, get_path

# Funkcja, która wypisuje na wyjście standardowe ścieżkę i rozmiar największego zasobu.
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
