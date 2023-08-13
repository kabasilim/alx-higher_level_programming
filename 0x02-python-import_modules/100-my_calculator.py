#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    argc = len(sys.argv)
    args = sys.argv

    if argc != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    else:
        a = int(args[1])
        b = int(args[3])

        if args[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif args[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif args[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif args[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            msg = "Unknown operator. Available operators: +, -, * and /"
            print("{}".format(msg))
            exit(1)


if __name__ == "__main__":
    main()
