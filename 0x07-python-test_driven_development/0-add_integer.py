!#usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def add_integer(a, b=98):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'

    a funtion that adds two integers
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

