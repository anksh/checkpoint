#!/usr/local/bin/python3

import os, sys


def _get_current_directory():
    return os.getcwd()

def add_checkpoint():
    # option 1: read file
    # find next unused entry
    # write to back of file
    # option 2: keep a global count
    # update count and write to back of file
    pass

def go_to_checkpoint(target):
    # find the checkpoint
    # cd to that checkpoint
    pass

def delete_checkpoint(victim):
    # read file
    # find checkpoint
    # remove it
    # rewrite file
    pass

def erase_all_checkpoints():
    # as simple as clearing the file
    pass

def list_checkpoints():
    # print out all checkpoints in a readable manner
    pass


def main():
    # look at sys args and decide which function needs to be called
    # if args are valid, return the chosen function
    # else throw/return None

    # different options:
    #     n: adds a new checkpoint
    #     <int>: goes to that directory (if it exists)
    #     d <int>: deletes a specific checkpoint - should prompt the user before doing so
    #     e: erases all checkpoints - should prompt the user before doing so
    #     l: list all checkpoints
    pass


if __name__ == '__main__':
    main()
