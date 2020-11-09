#! /usr/local/bin/python3.4

def loadFile(fileName):

    with open(fileName, "r") as aFile:
        lines = aFile.readlines()

    return lines

def getSummary():
    D1 = {}
    L1 = []
    L2 = []
    signals = []
    lines = loadFile("signals.txt")
    i = 0
    for items in lines:
        if i == 2:
            s = items.split()
            L1.append(s)
            L2.append(L1)
        elif i == 0:
            i += 1
            s = items.split()
            signals = s
        else:
            i += 1
    j = 1
    for items in signals:
        D1[items] = (0,0,0)

    return D1


def saveContinuousData(start, end, targetFileName):
    pass


def getSampledSignal(signalName):
    pass

def priceByVendor(file1, vendor, componentSet):
    i = 0
    lines = loadFile(file1)
    L2 = []
    L3 = []
    D1 = {}
    for items in lines:
        if i == 3:
            L1 = items.split(",")
            for j in L1:
                j = j.strip()
                L2.append(j)
            j = 0
            for c in componentSet:
                if L2[0] == c:
                    comp = L2[0]
                    price = L2[1]
                    L4 = [price, vendor]
                    D1[comp] = L4
            L2.clear()
        else:
            i += 1
    return D1

def identifyCheapest(componentSet):
    D1 = priceByVendor("CDW.txt", "CDW", componentSet)
    D2 = priceByVendor("eBay.txt", "eBay", componentSet)
    D3 = priceByVendor("GovConnection.txt", "GovConnection", componentSet)
    D4 = priceByVendor("Target.txt", "Target", componentSet)
    D5 = D1
    for k1,v1 in D5.items():
        for k2,v2 in D2.items():
            price1 = v1[0].split("$")
            price1 = price1[1]
            price2 = v2[0].split("$")
            price2 = price2[1]
            if price2 < price1:
                D5[k1] = v2
    for k1,v1 in D5.items():
        for k3,v3 in D3.items():
            price1 = v1[0].split("$")
            price1 = price1[1]
            price2 = v3[0].split("$")
            price2 = price2[1]
            if price2 < price1:
                D5[k1] = v3
    for k1,v1 in D5.items():
        for k4,v4 in D4.items():
            price1 = v1[0].split("$")
            price1 = price1[1]
            price2 = v4[0].split("$")
            price2 = price2[1]
            if price2 < price1:
                D5[k1] = v4
    return priceByVendor("CDW.txt", "CDW", componentSet)




def getComponentsToAdd():
    pass


if __name__ == "__main__":
    comp = {'Intel i7-4700HQ', 'Intel i7-6970HQ'}
    a = identifyCheapest(comp)
    print(a)
    b = getSummary()
    print(b)