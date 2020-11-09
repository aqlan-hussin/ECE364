#! /usr/local/bin/python3.4
import re

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    return lines

def parseXML(xmlNode):
    regex = r"\w+=\"[\w|\s]+\""
    attributes = re.findall(regex,xmlNode)
    myList = []
    for items in attributes:
        name = re.findall(r"(\w+)=",items)[0]
        value = re.findall(r"=\"([\w|\s]+)\"",items)[0]
        myTuple = (name, value)
        myList.append(myTuple)

    return sorted(myList)

def captureNumbers(sentence):
    regex = r"[+-]?\d{1}.\d+e[+-]?\d+|[+-]?\d+.\d+|[+-]?\d+"
    return re.findall(regex,sentence,re.IGNORECASE)

if __name__ == "__main__":
    xmlNode = '<person  name="Irene Adler" gender="female" age="35" />'
    print(parseXML(xmlNode))
    s = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023."
    print(captureNumbers(s))