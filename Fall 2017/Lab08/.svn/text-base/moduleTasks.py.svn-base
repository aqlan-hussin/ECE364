#! /usr/local/bin/python3.4
from exModule import runNetworkCode
import re
import glob

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()
    return lines

def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
        return True
    except ConnectionError:
        raise
    except OSError as e:
        return "An issue encountered during runtime. The name of the error is {0}".format(e.__class__.__name__)
    except:
        return False

def isOK(signalName):
    name = re.match(r'[A-Z]{3}\-[0-9]{3}$',signalName)
    if name is None:
        return False
    else:
        return True

def loadDataFrom(signalName, folderName):
    if isOK(signalName) == False:
        raise ValueError("{0} is invalid.".format(signalName))
    fileName = signalName + ".txt"
    filePath = glob.glob(folderName + "/" + fileName)
    if len(filePath) == 0:
        raise OSError("{0} file is missing".format(signalName))
    lines = loadFile(filePath[0])
    valid = []
    invalid = 0
    for items in lines:
        signal = re.findall(r'[-]?\d+\.\d+',items)
        if len(signal) == 0:
            invalid += 1
        else:
            valid.append(float(signal[0]))
    return (valid,invalid)

def isBounded(signalValues, bounds, threshold):
    if len(signalValues) == 0:
        raise ValueError("Signal contains no data.")
    max = 0
    for items in signalValues:
        if items < bounds[0] or items > bounds[1]:
            max += 1
        if max > threshold:
            return False
    return True

if __name__ == "__main__":
    print(checkNetwork())
    print(isOK('ABC-123'))
    print(loadDataFrom("AFW-481","Signals"))
    print(isBounded([1,2,3,4,5],(2,4),2))