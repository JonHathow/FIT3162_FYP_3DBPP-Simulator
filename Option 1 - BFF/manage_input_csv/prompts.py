# TODO: Evaluate documentation.

from .constants import ERROR_INTEGER, ERROR_BOOLEAN
from typing import Tuple

def prompt_integer(prompt: str) -> int:
    """ Reusable function to prompt user for a single integer input. """

    while True:
        try:
            n = int(input(f"\nDeclare the {prompt}: "))
            break
        except ValueError:
            print(ERROR_INTEGER)
    return abs(n)

def prompt_range(prompt: str) -> Tuple[int, int]:
    """ Reusable function to prompt user for a range of integer inputs. """

    while True:
        try:
            print(f"\nDeclare the range of {prompt}: ")
            a = int(input("Lower bound: "))
            b = int(input("Upper bound: "))
            break
        except ValueError:
            print(ERROR_INTEGER)
    return abs(a), abs(b)

def prompt_boolean(prompt: str) -> bool:
    """ Reusable function to prompt user for a string input to be translated to a corresponding boolean value. """
    while True:
        response = input(f"\nDo you want {prompt} (Y/N)? ")
        if response == "Y" or response == "y":
            x = True
            break
        elif response == "N" or response == "n":
            x = False
            break
        else:
            print(ERROR_BOOLEAN)  
    return x  