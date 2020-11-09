#! /usr/bin/env python3.4
import re
import glob

def isNameValid(signalName):
    name = re.match(r'[A-Z]{3}[-][0-9]{3}',signalName)
    if name is None:
        return False
    else:
        return True


def loadSignal(signalName, signalFolder):
    name = isNameValid(signalName)
    if name == False:
        raise ValueError("{} is invalid".format(signalName))
    file = signalName + ".txt"
    path = glob.glob(signalFolder + "/" + file)
    if len(path) == 0:
        raise OSError("{} file is missing".format(file))
    with open(path[0], 'r') as file1:
        line1 = file1.readlines()
    L1 = []
    invalid = 0
    for items in line1:
        signal = re.findall(r'[-]?[0-9]+[.][0-9]+',items)
        if len(signal) == 0:
            invalid += 1
        else:
            L1.append(float(signal[0]))
    return (L1,invalid)


def isSignalAcceptable(signal, valueRange, maxCount):
    if len(signal) == 0:
        raise ValueError("Signal contains no data")
    min = valueRange[0]
    max = valueRange[1]
    valid = 0
    invalid = 0
    for items in signal:
        if items < min or items > max:
            invalid += 1
        else:
            valid += 1
    if invalid <= maxCount:
        return True
    else:
        return False


if __name__ == "__main__":
    a = isNameValid("AFE-996")
    print(a)
    v,c = loadSignal("REY-386", "Signals")
    print(c)
    b = isSignalAcceptable(v, (-12.0,11.7), 20)
    print(b)