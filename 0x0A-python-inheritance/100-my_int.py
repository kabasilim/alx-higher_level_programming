#!/usr/bin/python3
"""MyInt Class"""


class MyInt(int):
    """MyInt Class"""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
