#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv)
    i = 0
    if argc == 2:
        i += 1
        print("{:d} argument:".format(argc - 1))
        print("{:d}: {}".format(i, sys.argv[i]))
    elif argc > 2:
        print("{:d} arguments:".format(argc - 1))
        i = 1
        while i < argc:
            print("{:d}: {}".format(i, sys.argv[i]))
            i += 1
    else:
        print("{:d} arguments.".format(0))


if __name__ == "__main__":
    main()
