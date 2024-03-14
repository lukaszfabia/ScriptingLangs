import sys


def read_std(func: callable, **kwargs) -> None:
    """reading from stdin

    Args:
        func (callable): function in which will be used stdin
        **kwargs: other parameters for function like: 
        * domain
        * start, end
        * etc. 
    """
    for line in sys.stdin:
        func(log=line, **kwargs)


def read_params(*args):
    """getting parameters from command line

    Returns:
        args: list of default parameters if there will be no parameters in line
    """
    if len(sys.argv) > 1:
        return sys.argv[1:]
    else:
        return args
