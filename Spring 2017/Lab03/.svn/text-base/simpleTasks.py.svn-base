#! /usr/local/bin/python3.4

def loadFile():

    with open("signals.txt", "r") as signalFile:
        lines = signalFile.readlines()

    return lines


def getAverageBySignal(signalName):
    filename = loadFile()
    signals = filename[0].split()
    i = 0
    sum = 0
    length = (len(filename) - 2)
    j = 0
    k = 0

    for items in signals:
        i += 1
        if items == signalName:
            k = i

    #print ('{}'.format(k))

    if k == 0:
        return "None"

    for lines in filename:
        if j == 2:
            num = lines.split()
            n = num[k]
            #print ('{}'.format(num))
            f = float(n)
            sum += f
        else:
            j += 1

    avg = sum/length

    return round(avg,2)


def getAverageByDay(day):
    filename = loadFile()
    j = 0
    line = 0
    i = 0
    sum = 0
    k = 0

    for lines in filename:
        if j == 2:
            num = lines.split()
            days = num[0]
            if days == day:
                i = line
        else:
            j += 1
        line += 1

    if i == 0:
        return "None"

    signals = filename[i].split()

    for items in signals:
        if k != 0:
            f = float(items)
            sum += f
        k =+ 1

    length = len(signals) - 1
    avg = sum/length

    return round(avg,2)


def split(l, n):

    if (isinstance(l, list)) and len(l) != 0:
        v = [l[x:x+n] for x in range(0, len(l), n)]
    else:
        v = "None"

    return v


def getPalindromes():
    l = []
    for i in range(99,999,1):
        for j in range(99,999,1):
            k = i * j
            if len(str(k)) == 6 and k == int(str(k)[::-1]):
                l.append(k)

    return sorted(set(l))


def getWords(sentence, c):
    s = sentence.split()
    l = []
    l2 = []
    for items in s:
        if items.startswith(c):
            l.append(items)
        if items.endswith(c):
            l.append(items)
    for items in l:
        if items not in l2:
            l2.append(items)

    return l2

def getCumulativeSum():
    l = []
    sum = 0
    for i in range(1,100,1):
        sum += i
        l.append(sum)

    return l


def transpose(mat):
    trans = [[x[i] for x in mat] for i in range(len(mat[0]))]
    return trans

def partition(stream):
    l = [int(s) for s in stream]
    j = 0
    l2 = []
    l3 = []
    for i in range(0,len(l)-1,1):
        j += 1
        l2.append(str(l[i]))
        if l[i] != l[i+1]:
            s = ''.join(l2)
            l2.clear()
            l3.append(s)
    return l3

def getTheSolution():
    pass

if __name__ == "__main__":
    a = getAverageBySignal("T1")
    print ('{}'.format(a))
    b = getAverageByDay("03/12")
    print ('{}'.format(b))
    v = [11, 18, 15, 21, 19, 13, 14, 17]
    c = split(v, 3)
    print ('{}'.format(c))
    d = getPalindromes()
    print(len(d))
    s = "the power of this engine matches that of the one we had last year"
    e = getWords(s,"t")
    print(e)
    f = getCumulativeSum()
    print(f)
    g = transpose([[9,1],[1,3],[3,1]])
    print(g)
    h = partition("0001111110111100000100")
    print(h)