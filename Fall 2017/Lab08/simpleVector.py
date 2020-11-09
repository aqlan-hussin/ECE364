#! /usr/local/bin/python3.4
import re

class Vector:

    def __init__(self, values):
        val = values.split()
        if len(val) != 2:
            raise ValueError("You must provide two values")
        self.x = float(val[0])
        self.y = float(val[1])
        pass

if __name__ == "__main__":
    a = Vector("0.1 3.14")
    print(a.x)
