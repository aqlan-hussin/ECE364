#! /usr/local/bin/python3.4

def getTotal(accounts):
    totalList = []
    for items in accounts:
        var = items.split('$')
        del var[0]
        total = 0
        for i,x in enumerate(var):
            x = x.strip()
            total += float(x)
        totalList.append(round(total,2))

    return totalList

def getDoublePalindromes():
    n = range(10,1000001)
    b10 = []
    for items in n:
        nList = list(str(items))
        length = len(nList)
        i = 0
        j = length-1
        boolList = []
        if length % 2 == 0:
            half = length/2
        else:
            half = (length-1)/2
        while i <= half-1:
            if nList[i] == nList[j]:
                boolList.append(True)
            else:
                boolList.append(False)
            i += 1
            j -= 1
        if False not in boolList:
            b10.append(items)

    b2 = []
    for num in b10:
        binary = "{0:b}".format(num)
        bList = list(str(binary))
        length = len(bList)
        i = 0
        j = length-1
        boolList = []
        if length % 2 == 0:
            half = length/2
        else:
            half = (length-1)/2
        while i <= half-1:
            if bList[i] == bList[j]:
                boolList.append(True)
            else:
                boolList.append(False)
            i += 1
            j -= 1
        if False not in boolList:
            b2.append(num)

    return b2

if __name__ == "__main__":
    accounts = ["George Teal:   $1.00    $2.00    $3.00  $4.01    ", "Christine Doyle:    $10.51  $22.49   $12.00    $5.33  $100.00"]
    print(getTotal(accounts))
    print(getDoublePalindromes())