#!/usr/local/bin/python3

import os


def get_directory():
    return os.getcwd()

def main():
    print(get_directory())


if __name__ == '__main__':
    main()
