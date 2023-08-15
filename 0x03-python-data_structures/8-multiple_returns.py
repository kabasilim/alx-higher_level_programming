#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_letter = None if not sentence or len == 0 else sentence[0]
    return (length, first_letter)
