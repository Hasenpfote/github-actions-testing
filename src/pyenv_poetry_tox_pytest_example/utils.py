import sys


def add(a, b):
    '''Adds two numbers.
    Args:
        a: The value of the left-hand side.
        b: The value of the right-hand side.
    Returns
        The resulting value.
    '''
    return a + b


def sub2(a, b):
    return a - b


def print_greet():
    '''Displays greeting.'''
    print('Hello, world!')


def print_python_version():
    '''Displays python version.'''
    # print(f"{sys.version=}")  # Syntax for Python 3.8 or higher.
    print(f"sys.version={sys.version}")
    # print(sys.version)


if __name__ == '__main__':
    print_greet()
