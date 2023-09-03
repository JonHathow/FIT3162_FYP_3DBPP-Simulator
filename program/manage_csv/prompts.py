""" 
Functions to prompt users for inputs of various types. Different strings can be
plugged in to alter the input request statement. Such arguments (with the prefix
PROMPT_) can be found in constants.py.
"""

from .constants import ERROR_NUMBER, ERROR_INTEGER, ERROR_BOOLEAN
from typing import Tuple


# needed for testing
def get_input(prompt: str) -> str:
    return input(prompt)

# needed for testing
def get_input2(prompt: str) -> str:
    return input(prompt)

def prompt_number(prompt: str) -> float:
    """ Reusable function to prompt user for a single numerical input. """

    while True:
        try:
            n = float(get_input(f"\nDeclare the {prompt}: "))
            break
        except ValueError:
            print(ERROR_NUMBER)
    return abs(n)

def prompt_integer(prompt: str) -> int:
    """ Reusable function to prompt user for a single integer input. """

    while True:
        try:
            n = int(get_input(f"\nDeclare the {prompt}: "))
            break
        except ValueError:
            print(ERROR_INTEGER)
    return abs(n)

def prompt_range(prompt: str) -> Tuple[int, int]:
    """ 
    Reusable function to prompt user for two numerical inputs:
    a lower and upper bound for a certain range of values.
    """

    while True:
        try:
            print(f"\nUsing only integers, declare the range of {prompt}: ")
            a = int(get_input("Lower bound: "))
            b = int(get_input2("Upper bound: "))
            break
        except ValueError:
            print(ERROR_INTEGER)
    return abs(a), abs(b)

def prompt_boolean(prompt: str) -> bool:
    """ 
    Reusable function to prompt user for a string input to be translated
    to a corresponding boolean value.
    """

    while True:
        response = get_input(f"\nDo you want {prompt} (Y/N)? ")
        if response == "Y" or response == "y":
            return True
        elif response == "N" or response == "n":
            return False
        else:
            print(ERROR_BOOLEAN)  

"""
def prompt_number(prompt: str) -> float:

    while True:
        try:
            n = int(input(f"\nDeclare the {prompt}: "))
            break
        except ValueError:
            print(ERROR_NUMBER)
    return abs(n)
"""