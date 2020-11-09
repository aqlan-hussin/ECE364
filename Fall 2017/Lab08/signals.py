#! /usr/local/bin/python3.4
from moduleTasks import *

def loadMultiple(signalNames, folderName, maxCount):
    dict = {}
    for items in signalNames:
        try:
            data = loadDataFrom(items, folderName)
            if data[1] <= maxCount:
                dict[items] = data[0]
            else:
                dict[items] = []
        except:
            dict[items] = None

    return dict

def saveData(signalsDictionary, targetFolder, bounds, threshold):
    for k,v in signalsDictionary.items():
        filePath = targetFolder + "/" + k + ".txt"
        invalid = 0
        if v is not None and len(v) != 0:
            for items in v:
                if items < bounds[0] or items > bounds[1]:
                    invalid += 1
            if invalid <= threshold:
                with open(filePath, 'w') as myFile:
                    for signal in v:
                        myFile.write("{0:.3f}\n".format(signal))

if __name__ == "__main__":
    print(loadDataFrom("GUO-758","Signals"))
    a = loadMultiple(["AFW-481","ABC-1234","ABC-123","GUO-758"],"Signals",5)
    print(a)
    saveData(a,"Save",[-6.0,6.0],10)
