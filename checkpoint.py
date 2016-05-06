#!/usr/bin/python

import os, getopt, subprocess, sys
from StringIO import StringIO

DATAFILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/.checkpoints.txt"

def _get_current_directory():
    return os.getcwd()

def add_checkpoint():
    # update count and write new checkpoint to back of file
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

    target = int(target)

    data_file = open(DATAFILE_PATH, 'r')
    num_entries = int(data_file.readline())
    if target > num_entries:
        print "Invalid checkpoint number, try listing all the checkpoints as a double check!"
        return

    for x in xrange(1, target):
        data_file.readline()

    target_line = data_file.readline()
    target_dir = target_line.split(' ', 1)[1]
    target_dir = target_dir[:-1] # removing newline character
    subprocess.call(['cd', target_dir])

    data_file.close()
    print target_dir
    # print "Switched to checkpoint number " + str(target) + " at " + target_dir

def delete_checkpoint(victim):
    # read file
    # find checkpoint
    # remove it
    # rewrite file

    victim = int(victim)

    data_file = open(DATAFILE_PATH, 'r')
    num_entries = int(data_file.readline())
    new_entries = str(num_entries - 1)

    if victim > num_entries:
        print "Invalid checkpoint number, try listing all the checkpoints as a double check!"
        return

    file_buf = StringIO()
    file_buf.write(new_entries.zfill(10) + '\n')

    victim_dir = None
    for line in data_file.readlines():
        split_line = line.split(' ', 1)
        index = int(split_line[0])
        if victim_dir:
            index -= 1
            file_buf.write(str(index) + ' ' + split_line[1])
        else:
            if index == victim:
                victim_dir = split_line[1]
            else:
                file_buf.write(line)

    data_file.close()
    data_file = open(DATAFILE_PATH, 'w')
    data_file.write(file_buf.getvalue())
    data_file.close()
    file_buf.close()

    print "Removed checkpoint number " +  str(victim)  + " at " + victim_dir[:-1]

def erase_all_checkpoints():
    # as simple as clearing the file

    data_file = open(DATAFILE_PATH, 'w')
    data_file.write('0')
    data_file.close()

    print "Cleared all checkpoints"

def list_checkpoints():
    # print out all checkpoints in a readable manner

    data_file = open(DATAFILE_PATH, 'r')

    num_entries = int(data_file.readline())

    print "Listing " + str(num_entries) + " checkpoints..."

    for line in data_file.readlines():
        split_line = line.split(' ', 1)
        print "Checkpoint #" + split_line[0] + ":\t" + split_line[1] ,

    data_file.close()



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
