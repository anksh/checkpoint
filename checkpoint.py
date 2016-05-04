#!/usr/bin/python

import os, getopt, sys

def _get_current_directory():
    return os.getcwd()

def add_checkpoint():
    # update count and write to back of file
    # return number of checkpoint and the directory that was added
    pass

def go_to_checkpoint(target):
    # find the checkpoint
    # cd to that checkpoint
    # return the checkpoint that we just went to
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

    try:
        opts, args = getopt.getopt(sys.argv[1:], "nc:r:elh")
    except getopt.GetoptError as e:
        print e
        sys.exit(1)

    if args:
        print "The argument, " + str(args[0]) + ", that you passed in was ignored, possibly along with other bad arguments."
        print "Please pass in the -h flag for more info on how to use this script."

    for o, a in opts:
        print "Option: " + o
        if a:
            print "Argument: " + str(a)

        # different options:
        if o == "-n":
            print "Added a new checkpoint number _______ at __________"
            # n: adds a new checkpoint
            pass
        elif o == "-c":
            print "Switched to checkpoint number _____ "
            # c <int>: goes to that directory (if it exists)
            pass
        elif o == "-r":
            print "Removed checkpoint number ___ at _________ "
            # r <int>: removes a specific checkpoint - should prompt the user before doing so
            pass
        elif o == "-e":
            print "Cleared all checkpoints"
            # e: erases all checkpoints - should prompt the user before doing so
            pass
        elif o == "-l":
            print "LIST OF CKPTS"
            # l: list all checkpoints
            pass
        elif o == "-h":
            print "Help coming soon"
            # h: help
            pass
        else:
            print "Yeah something fucked up, this is not a valid option"
            # shouldnt get here but just in case a helpful error message
            pass

if __name__ == '__main__':
    main()
