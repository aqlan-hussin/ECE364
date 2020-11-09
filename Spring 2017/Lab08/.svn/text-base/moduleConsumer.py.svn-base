#! /usr/bin/env python3.4
from moduleTasks import *

def loadSignals(signalNames, signalFolder, maxNonfloatCount):
    dict = {}
    for name in signalNames:
        try:
            v,c = loadSignal(name, signalFolder)
        except:
            dict[name] = None
        if c <= maxNonfloatCount:
            dict[name] = v
        else:
            dict[name] = []
    return dict


def saveSignals(signalsDictionary, valueRange, maxCount, targetFolder):
    min = valueRange[0]
    max = valueRange[1]
    invalid = 0
    for key,val in signalsDictionary.items():
        if val != None and len(val) != 0:
            for items in val:
                if items < min or items > max:
                    invalid += 1
            if invalid < maxCount:
                with open(targetFolder + "/" + key + ".txt", 'w') as file1:
                    for item in val:
                        file1.write("{0:.3f}\n".format((item)))
    pass


if __name__ == "__main__":
    s = ["REY-386","PVL-758"]
    d = loadSignals(s,"Signals", 6)
    saveSignals(d,(-12.0,11.7),20,"Target")