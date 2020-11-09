#! /usr/bin/env python3.4
from operations import *
import re

def getTotalDuration(eventName):
    with open("Events.txt") as file1:
        lines = file1.readlines()
    i = 0
    hours = 0
    for items in lines:
        if i == 2:
            comp = items.split()
            name = comp[0]
            duration = comp[1]
            mult = comp[2]
            if name == eventName:
                if 'w' in duration:
                    n = int(re.findall(r'[0-9]+',duration)[0])
                    hours += (24 * 7 * n * int(mult))
                if 'd' in duration:
                    n = int(re.findall(r'[0-9]+',duration)[0])
                    hours += (24 * n * int(mult))
                if 'h' in duration:
                    n = int(re.findall(r'[0-9]+',duration)[0])
                    hours += (n * int(mult))
        else:
            i += 1
    return Duration(0,0,hours)

def rankEventsByDuration(*args):
    D1 = {}
    L1 = []
    L2 = []
    for items in args:
        duration = getTotalDuration(items)
        hours = duration.getTotalHours()
        name = items
        D1[name] = hours
        L1.append(hours)
    i = 0
    for items in sorted(L1,reverse=True):
        for key,val in D1.items():
            if val == items:
                L2.append(key)
    return L2

if __name__ == "__main__":
    a = getTotalDuration("Event17")
    print(a)
    b = rankEventsByDuration("Event01", "Event02", "Event03")
    print(b)