#! /usr/local/bin/python3.4

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    return lines

def getAvailability():
    lines = loadFile("Availability.txt")
    dict = {}
    i = 0
    dateList = []
    for items in lines:
        if i != 0 and i != 1 and i != 2:
            v = items.split('|')
            avaList = []
            j = 0
            k = 0
            for s in v:
                if j != 0:
                    if s.strip() == '1':
                        avaList.append(dateList[k])
                    k += 1
                else:
                    j += 1
            dict[v[0].strip()] = avaList
        elif i == 1:
            v = items.split()
            j = 0
            for d in v:
                if j != 0 and j != 1:
                    dateList.append(d)
                else:
                    j += 1
            i += 1
        else:
            i += 1
    return dict

def getDateList():
    lines = loadFile("Availability.txt")
    dict = {}
    i = 0
    dateList = []
    for items in lines:
        if i != 0 and i != 1 and i != 2:
            v = items.split('|')
            avaList = []
            j = 0
            k = 0
            for s in v:
                if j != 0:
                    if s.strip() == '1':
                        avaList.append(dateList[k])
                    k += 1
                else:
                    j += 1
            dict[v[0].strip()] = avaList
        elif i == 1:
            v = items.split()
            j = 0
            for d in v:
                if j != 0 and j != 1:
                    dateList.append(d)
                else:
                    j += 1
            i += 1
        else:
            i += 1
    return dateList

def getFreeByName(names):
    avaDict = getAvailability()
    freeDict = {}
    for name in names:
        for k,v in avaDict.items():
            if name == k:
                freeDict[name] = v
    return freeDict

def getFreeByRange(date1, date2):
    m1 = date1.split('/')[0]
    d1 = date1.split('/')[1]
    m2 = date2.split('/')[0]
    d2 = date2.split('/')[1]
    if int(m2) < int(m1):
        return None
    elif int(m1) == int(m2) and int(d2) < int(d1):
        return None
    dateList = getDateList()
    idx1 = dateList.index(date1)
    idx2 = dateList.index(date2)
    dateRange = dateList[idx1:idx2+1]
    avaDict = getAvailability()
    a = 1
    nameList = []
    print(dateRange)
    for k,v in avaDict.items():
        for date in dateRange:
            if date not in v:
                a = 0
        if a == 1:
            nameList.append(k)
    return set(nameList)

def getZipStateDict():
    lines = loadFile("ZipCodes.txt")
    dict = {}
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            dict[v[2]] = v[0]
        else:
            i += 1
    return dict

def getZipLatLongDict():
    lines = loadFile("LatLong.txt")
    dict = {}
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            mylist = []
            mylist.append(v[0])
            mylist.append(v[1])
            dict[v[2]] = mylist
        else:
            i += 1
    return dict

def getCountyList():
    lines = loadFile("Counties.txt")
    cList = []
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            if v[2] not in cList:
                cList.append(v[2])
        else:
            i += 1
    return cList

def getStateByCounty(county):
    if county not in getCountyList():
        return set()
    lines = loadFile("Counties.txt")
    latlongDict = getZipLatLongDict()
    zipList = []
    i = 0
    for items in lines:
        mylist = []
        if i != 0 and i != 1:
            v = items.split()
            mylist.append(v[0])
            mylist.append(v[1])
        else:
            i += 1
        for k,v in latlongDict.items():
            if mylist == v:
                zipList.append(k)
    stateDict = getZipStateDict()
    stateList = []
    for k,v in stateDict.items():
        for items in zipList:
            if k == items:
                stateList.append(v)
    return set(stateList)

if __name__ == "__main__":
    print(getFreeByName({'Sang, Chanell', 'Chock, Velvet'}))
    print(getFreeByRange("08/08", "08/12"))
    print(getZipLatLongDict())
    print(getStateByCounty("Summit"))
