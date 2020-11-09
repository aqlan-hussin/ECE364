#! /usr/local/bin/python3.4
from simpleVector import *

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()
    return lines

def loadVectors(fileName):
    lines = loadFile(fileName)
    vectorList = []
    for items in lines:
        try:
            v = Vector(items)
            vectorList.append(v)
        except:
            vectorList.append(None)
    return vectorList

if __name__ == "__main__":
    a = loadVectors("values.txt")
    print(len(a))
