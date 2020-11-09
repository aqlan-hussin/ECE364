#! /usr/bin/env python3.4
import re

def getPhone(line):
    regex = r'[0-9]{3}[-]?[0-9]{3}[-]?[0-9]{4}'
    list = re.findall(regex,line)
    return list[0]

if __name__ == "__main__":
    print(getPhone("I got a call today from 765-890-1234 that I did not recognize."))
    print(getPhone("Call the help-desk at 8009994312."))
