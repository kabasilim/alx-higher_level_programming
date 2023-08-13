#!/usr/bin/python3
import sys


def main():
    i = len(sys.argv)
    arg_sum = 0
    counter = 1

    while counter < i:
        arg_sum += int(sys.argv[counter])
        counter += 1
    print("{:d}".format(arg_sum))


if __name__ == "__main__":
    main()
