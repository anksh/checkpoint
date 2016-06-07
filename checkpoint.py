#!/usr/bin/python

import os
import getopt
import subprocess
import sys
import pickle

DATAFILE_PATH = os.path.dirname(
    os.path.abspath(__file__)) + "/.checkpoints.txt"

"""
Structure of checkpoints dictionary:
{
    count: "filepath",
}
"""


def _get_current_directory():
    return os.getcwd()


def add_checkpoint():
    """
    update count and write new checkpoint to back of file
    return number of checkpoint and the directory that was added
    """
    cwd = _get_current_directory()
    checkpoints = load_checkpoints()

    checkpoint_id = len(checkpoints)
    checkpoints[checkpoint_id] = cwd

    save_checkpoints(checkpoints)

    print "Added new checkpoint:\n\t{}:\t{}".format(checkpoint_id, cwd)


def go_to_checkpoint(target):
    """
    find the checkpoint
    cd to that checkpoint
    """

    checkpoint_id = int(target)

    checkpoints = load_checkpoints()

    if checkpoint_id not in checkpoints:
        print "Invalid checkpoint number. Try listing all the checkpoints to double check!"
        return

    target_dir = checkpoints[checkpoint_id]
    subprocess.call(['cd', target_dir])

    save_checkpoints(checkpoints)
    print target_dir


def delete_checkpoint(victim):
    """
    read file
    find checkpoint
    remove it
    rewrite file
    """

    checkpoint_id = int(victim)

    checkpoints = load_checkpoints()

    if checkpoint_id in checkpoints:
        loc = checkpoints[checkpoint_id]  # only for printing
        del checkpoints[checkpoint_id]
        print "Removed checkpoint:\n\t{}:\t{}".format(checkpoint_id, loc)
        return

    print "Invalid checkpoint number. Try listing all the checkpoints to double check!"


def erase_all_checkpoints():
    # as simple as clearing the file

    checkpoints = dict()
    save_checkpoints(checkpoints)    

    print "Cleared all checkpoints"


def list_checkpoints():
    # print out all checkpoints in a readable manner

    checkpoints = load_checkpoints()

    print "Listing all checkpoints:"
    for checkpoint_id, path in checkpoints:
        print "{}:\t{}".format(checkpoint_id, path)
    


def load_checkpoints():
    """
    Loads the checkpoints dictionary from the pickled file or creates a new one if it doesnt exist.
    """
    try:
        checkpoints = pickle.load(DATAFILE_PATH)
    except Exception, e:
        checkpoints = dict()
    else:
        if not checkpoints:
            checkpoints = dict()

    return checkpoints


def save_checkpoints(checkpoints):
    """
    Dumps the checkpoints dict to the file
    """
    pickle.dump(checkpoints, DATAFILE_PATH)


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
        # print "Option: " + o
        if a:
            pass
            # print "Argument: " + str(a)

        # different options:
        if o == "-n":
            # n: adds a new checkpoint
            add_checkpoint()

        elif o == "-c":
            # c <int>: goes to that directory (if it exists)
            go_to_checkpoint(a)

        elif o == "-r":
            # r <int>: removes a specific checkpoint - should prompt the user
            # before doing so
            delete_checkpoint(a)

        elif o == "-e":
            # e: erases all checkpoints - should prompt the user before doing
            # so
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
