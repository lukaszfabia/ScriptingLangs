def print_output(**kwargs) -> None:
    """prints the output of the program
    * param kwargs: key=tag, value=result
    * return: None
    """
    for key, value in kwargs.items():
        print(f'{key}: {value}')
