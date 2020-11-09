#! /usr/local/bin/python3.4

def loadFile(fileName):

    with open(fileName, "r") as aFile:
        lines = aFile.readlines()

    return lines

def isValidOutput(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    lines = loadFile(fileName)
    i = 0
    L1 = []
    for items in lines:
        items = items.strip()
        L2 = [int(d) for d in str(items)]
        L1.append(L2)
    vRow = 0
    vCol = 0
    for m in L1:
        j = 0
        for n in m:
            j += 1
            if j in m:
                vRow += 1
    k = 0
    L2 = []
    while k < 9:
        for m in L1:
            L2.append(m[k])
        j = 0
        for n in L2:
            if j in L2:
                vCol += 1
        L2.clear()
        k += 1
    if vRow == 81 and vCol == 81:
        return True
    else:
        return False

def isColumnPuzzle(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    lines = loadFile(fileName)
    L1 = []
    for items in lines:
        items = items.strip()
        L2 = [d for d in items]
        L1.append(L2)
    for items in L1:
        if '.' in items:
            x = True
        else:
            x = False
    return x

def solveColPuzzle(source, target):
    lines = loadFile(source)
    i = 1
    j = 0
    L1 = []
    for items in lines:
        items = items.strip()
        L2 = [d for d in items]
        L1.append(L2)
    for items in L1:
        L3 = items
        n = 0
        i = 1
        while i <= 9:
            if str(i) not in L3:
                n = str(i)
            i += 1
        j = 0
        while j < 9:
            if items[j] == '.':
                L3[j] = n
            j += 1
    file1 = open(target, "w")
    for x in L1:
        for y in x:
            file1.write(str(y))
        file1.write("\n")
    file1.close()
    return


def solveRowPuzzle(source, target):
    lines = loadFile(source)
    i = 0
    L1 = []
    L3 = []
    file1 = open("inter.sud", "w")
    for items in lines:
        items = items.strip()
        L2 = [d for d in str(items)]
        L1.append(L2)
    L2 = []
    k = 0
    n = 0
    while k < 9:
        for m in L1:
            L2.append(m[k])
        i = 0
        while i <= 9:
            if str(i) not in L2:
                n = str(i)
            i += 1
        j = 0
        while j < 9:
            if L2[j] == '.':
                L2[j] = n
            j += 1
        for x in L2:
            file1.write(str(x))
        file1.write("\n")
        L2.clear()
        k += 1
    file1.close()
    i = 0
    with open ("inter.sud", "r") as file1:
        lines1 = file1.readlines()
    file2 = open(target, "w")
    for items in lines1:
        items = items.strip()
        L2 = [int(d) for d in str(items)]
        L3.append(L2)
    L4 = []
    while i < 9:
        for m in L3:
            L4.append(m[i])
        i += 1
    i = 0
    for x in L4:
        file2.write(str(x))
        i += 1
        if i == 9:
            file2.write("\n")
            i = 0
    file1.close()
    file2.close()
    return

def solvePuzzle(sourceFileName, targetFileName):

    # TODO: Remove the "pass" before you add any code to this block.
    cate = isColumnPuzzle(sourceFileName)
    if cate == True:
        solveColPuzzle(sourceFileName, targetFileName)
    else:
        solveRowPuzzle(sourceFileName, targetFileName)
    return

def getCallersOf(phoneNumber):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def getCallActivity():

    # TODO: Remove the "pass" before you add any code to this block.
    pass


if __name__ == "__main__":
    a = isValidOutput("invalid2.sud")
    print(a)
    b = isColumnPuzzle("open1.sud")
    print(b)
    solvePuzzle("open1.sud", "answer1.sud")
    solvePuzzle("open2.sud", "answer2.sud")