#! /usr/local/bin/python3.4
import re

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()
    return lines

def parseSimple(fileName):
    dict = {}
    lines = loadFile(fileName)
    for items in lines:
        fields = re.findall(r'\"[^\"]+\"',items)
        if len(fields) != 0:
            key = re.findall(r'[^\"]+',fields[0])[0]
            val = re.findall(r'[^\"]+',fields[1])[0]
            dict[key] = val
    return dict


def parseLine(fileName):
    dict = {}
    lines = loadFile(fileName)
    for items in lines:
        fields = re.findall(r'\"[^\"]+\"',items)
        i = 0
        while i < len(fields):
            key = re.findall(r'[^\"]+',fields[i])[0]
            val = re.findall(r'[^\"]+',fields[i+1])[0]
            dict[key] = val
            i += 2
    return dict


def parseComplex(fileName):
    dict = {}
    lines = loadFile(fileName)
    for items in lines:
        fields = re.findall(r'\"[^\"]+\"|true|false|[-]?\d+\.\d+|[-]?\d+',items)
        if len(fields) != 0:
            key = re.findall(r'[^\"]+',fields[0])[0]
            val = re.findall(r'[^\"]+',fields[1])[0]
            if val == 'false':
                val = False
            if val == 'true':
                val = True
            dict[key] = val
    return dict


def parseComposite(fileName):
    pass


if __name__ == "__main__":
    print(parseSimple("simple.json"))
    print(parseLine("simple2.json"))
    print(parseComplex("complex.json"))
