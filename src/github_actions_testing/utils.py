import sys
import time


def add(a, b):
    '''Adds two numbers.
    Args:
        a: The value of the left-hand side.
        b: The value of the right-hand side.
    Returns
        The resulting value.
    '''
    return a + b


def sub(a, b):
    '''Subtracts two numbers.
    Args:
        a: The value of the left-hand side.
        b: The value of the right-hand side.
    Returns
        The resulting value.
    '''
    return a - b


def mul(a, b):
    '''Multiplies two numbers.
    Args:
        a: The value of the left-hand side.
        b: The value of the right-hand side.
    Returns
        The resulting value.
    '''
    return a * b


def div(a, b):
    '''Divides two numbers.
    Args:
        a: The value of the left-hand side.
        b: The value of the right-hand side.
    Returns
        The resulting value.
    '''
    return a / b


def muladd(a, b, c):
    '''Performs the fused multiply-add operation.'''
    return a * b + c


def print_greet():
    '''Displays greeting.'''
    print('Hello, world!')


def print_python_version():
    '''Displays python version.'''
    if sys.version_info < (3, 8):
        print(f"sys.version={sys.version}")
    else:
        print(f"sys.version={sys.version}")

    # print(f"{sys.version=}")  # Syntax for Python 3.8 or higher.
    # print(f"sys.version={sys.version}")
    # print(sys.version)


def print_with_delay(text):
    delay = len(text) / 100 + 1.0
    time.sleep(delay)
    print(text)


if __name__ == '__main__':
    print_greet()