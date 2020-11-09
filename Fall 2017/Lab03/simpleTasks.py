#! /usr/local/bin/python3.4

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    return lines

def mult(list):
    p = 1
    for i in list:
        p *= i
    return p

def find(pattern):
    line = loadFile("sequence.txt")
    line = line[0]
    #line = "138389"
    lenP = len(pattern)
    lenS = len(line)
    strList = []
    ptnList = list(pattern)
    i = 0

    while i <= lenS - lenP:
        myStr = line[i:i+lenP]
        strList.append(myStr)
        i += 1

    countX = ptnList.count("X")
    x = ["0","1","2","3","4","5","6","7","8","9"]
    import itertools
    xList = [''.join(a) for a in itertools.product(x, repeat=countX)]

    patternList = []
    for y in xList:
        yList = list(y)
        ptnCopy = ptnList.copy()
        j = 0
        for index,items in enumerate(ptnCopy):
            if items == "X":
                ptnCopy[index] = yList[j]
                j += 1
        patternList.append(''.join(ptnCopy))

    myList = []
    for items in patternList:
        if items in strList:
            myList.append(items)

    return myList

def getStreakProduct(sequence, maxSize, product):
    i = 0
    strList = []
    while i <= len(sequence):
        j = i+1
        k = 0
        x = ""
        while k < maxSize:
            myStr = sequence[i:j]
            if myStr != x:
                strList.append(myStr)
            x = myStr
            j += 1
            k += 1
        i += 1

    myList = []
    for items in strList:
        itemList = list(items)
        for index,n in enumerate(itemList):
            itemList[index] = int(n)
        p = mult(itemList)
        if p == product:
            myList.append(items)

    return myList

def writePyramids(filePath, baseSize, count, char):
    line = []
    i = 0
    while i <= baseSize:
        line.append(" ")
        i += 1
    height = (baseSize + 1) / 2
    center = int(height)
    j = 0
    myList = []
    while j < height:
        line[center+j] = char
        line[center-j] = char
        k = 0
        copy = []
        while k < count:
            for items in line:
                copy.append(items)
            k += 1
        copy.remove(" ")
        myList.append(''.join(copy))
        j += 1

    myList.append("")
    with open(filePath, "w") as myFile:
        myFile.writelines("\n".join(myList))

    return

def getStreaks(sequence, letters):
    alphabets = list(letters)
    seqList = list(sequence)
    seqList.append("")
    prev = ""
    i = 0
    wordList = []
    for index,items in enumerate(seqList):
        if items != prev:
            word = ''.join(seqList[i:index])
            wordList.append(word)
            i = index
        prev = items

    wordList.remove("")
    myList = []
    for items in wordList:
        c = list(items)
        if c[0] in alphabets:
            myList.append(items)

    return myList

def findNames(nameList, part, name):
    myList = []
    for items in nameList:
        s = items.lower().split()
        if part == "F":
            if s[0] == name.lower():
                myList.append(items)
        elif part == "L":
            if s[1] == name.lower():
                myList.append(items)
        elif part == "FL":
            if s[0] == name.lower():
                myList.append(items)
            if s[1] == name.lower():
                myList.append(items)

    return myList

def convertToBoolean(num, size):
    if type(num) is not int:
        return []
    binary = "{0:b}".format(num)
    binList = list(binary)
    for index,items in enumerate(binList):
        if items == "1":
            binList[index] = True
        else:
            binList[index] = False

    while len(binList) < size:
        binList.insert(0,False)

    return binList

def convertToInteger(boolList):
    if type(boolList) is not list:
        return None
    if len(boolList) == 0:
        return None
    for index,items in enumerate(boolList):
        if items == True:
            boolList[index] = "1"
        elif items == False:
            boolList[index] = "0"
        else:
            return None
    binStr = ''.join(boolList)
    n = int(binStr,2)

    return n

if __name__ == "__main__":
    str = "138389"
    pattern = "X141X"
    a = find(pattern)
    print(a)
    b = getStreakProduct("54789654321687984",6,288)
    print(b)
    writePyramids('pyramid9.txt',13,6,'X')
    c = getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS","PAZ")
    print(c)
    names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    d = findNames(names, "FL", "Johnson")
    print(d)
    e = convertToBoolean(9,3)
    print(e)
    bList = [True, False, False, False, False, True, True, True]
    f = convertToInteger(e)
    print(f)