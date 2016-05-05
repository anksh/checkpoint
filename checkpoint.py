#!/usr/bin/python

import os, getopt, sys
from StringIO import StringIO

DATAFILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/.checkpoints.txt"

def _get_current_directory():
    return os.getcwd()

def add_checkpoint():
    # update count and write to back of file
    # return number of checkpoint and the directory that was added
    cwd = _get_current_directory()
    data_file = open(DATAFILE_PATH, 'r')
    data_buf = StringIO(data_file.read())
    data_file.close()
    num_entries = int(data_buf.readline())
    new_entries = num_entries + 1
    new_entries = str(new_entries)
    data_buf.seek(0)
    data_buf.write(new_entries.zfill(10) + '\n')
    to_write = str(new_entries)+ ' ' + cwd + '\n'
    data_buf.seek(0, os.SEEK_END)
    data_buf.write(to_write)
    data_file = open(DATAFILE_PATH, 'w')
    data_file.write(data_buf.getvalue())
    data_file.close()
    data_buf.close()

    print "Added a new checkpoint number " + str(new_entries) + " at " + cwd

def go_to_checkpoint(target):
    # find the checkpoint
    # cd to that checkpoint
    # return the checkpoint that we just went to
    print "Switched to checkpoint number _____ "

def delete_checkpoint(victim):
    # read file
    # find checkpoint
    # remove it
    # rewrite file
    print "Removed checkpoint number ___ at _________ "

def erase_all_checkpoints():
    # as simple as clearing the file
    print "Cleared all checkpoints"

def list_checkpoints():
    # print out all checkpoints in a readable manner
    print "LIST OF CKPTS"


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
        print "Please pass in the -h flag for more info on how to use this script.\n"

    if not opts:
        print "No options were passed in."
        print "Please pass in the -h flag for more info on how to use this script.\n"

    for o, a in opts:
        print "Option: " + o
        if a:
            print "Argument: " + str(a)

        # different options:
        if o == "-n":
            # n: adds a new checkpoint
            add_checkpoint()

        elif o == "-c":
            # c <int>: goes to that directory (if it exists)
            go_to_checkpoint(a)

        elif o == "-r":
            # r <int>: removes a specific checkpoint - should prompt the user before doing so
            delete_checkpoint(a)

        elif o == "-e":
            # e: erases all checkpoints - should prompt the user before doing so
            erase_all_checkpoints()

        elif o == "-l":
            # l: list all checkpoints
            list_checkpoints()

        elif o == "-h":
            # h: help
            print "Help coming soon"

        else:
            # shouldnt get here but just in case a helpful error message
            print "Yeah something fucked up, this is not a valid option"

if __name__ == '__main__':
    main()
