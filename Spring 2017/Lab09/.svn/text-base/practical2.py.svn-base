#! /usr/bin/env python3.4
import re

def getNumericData(sentence):
    L1 = []
    integers = re.findall(r'[+-]?[0-9]+',sentence)
    for items in integers:
        L1.append(items)
    regF = re.findall(r'[+-]?[0-9]+.[0-9]+',sentence)
    for items in regF:
        L1.append(items)
    sciN = re.findall((r'[+-]?[0-9].[0-9]+[eE][+-][0-9]+'),sentence)
    for items in sciN:
        L1.append(items)
    return L1

def parseSimple(fileName):
    D1 = {}
    with open(fileName) as file1:
        lines = file1.readlines()
    for items in lines:
        if "{" not in items and "}" not in items:
            key = re.findall(r'[ ]*"[a-zA-z]+"[ ]*:',items)
            val = re.findall(r':[ ]*".*",?',items)
            k = re.findall(r'[^ ":]+',key[0])
            v1 = re.findall(r'".*"',val[0])
            v2 = re.findall(r'[^"]+',v1[0])
            D1[k[0]] = v2[0]
    return D1


def parseLine(fileName):
    D1 = {}
    L1 = []
    L2 = []
    with open(fileName) as file1:
        lines = file1.readlines()
    for items in lines:
        key = re.findall(r'[ ]*"[a-zA-z]+"[ ]*:',items)
        val = re.findall(r':".*",?',items)
        v1 = re.findall(r'[^"]+',items)
    for items in key:
        k = re.findall(r'[^ ":]+',items)
        L1.append(k[0])
    prev = " "
    for items in v1:
        if prev == ':':
            v2 = items
            L2.append(v2)
        prev = items
    i = 0
    while i < len(L1):
        k1 = L1[i]
        v3 = L2[i]
        D1[k1] = v3
        i += 1
    return D1


def parseComplex(fileName):
    pass


def parseComposite(fileName):
    pass


if __name__ == "__main__":
    s = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023."
    print(getNumericData(s))
    a = parseSimple("simple.json")
    print(a)
    b = parseLine("simple2.json")
    print(b)