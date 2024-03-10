def print_output(**kwargs):
    """function to print the output of the program
    * param kwargs: key=description, value=result
    * return: None
    """
    for key, value in kwargs.items():
        print(f'{key}: {value}')
