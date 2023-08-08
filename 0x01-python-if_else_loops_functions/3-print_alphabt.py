#!/usr/bin/python3
for char in range(ord("a"), ord("z") + 1):
    if char != 101 and char != 113:
        print("{}".format(chr(char)), end="")
