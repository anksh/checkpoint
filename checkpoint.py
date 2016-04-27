#!/usr/local/bin/python3

import os, sys


def get_directory(*args):
    return os.getcwd()


def choose_function():
#   look at sys args and decide which function needs to be called
#   if args are valid, return the chosen function
#   else throw/return None
    if(len(sys.argv) != 1):
        raise RuntimeError()
    return get_directory

def main():
    try:
        chosen_function = choose_function()
    except RuntimeError:
        print("Invalid input! Please use the -h flag for more info")
        return

    print(chosen_function(sys.argv[1:]))

if __name__ == '__main__':
    main()
