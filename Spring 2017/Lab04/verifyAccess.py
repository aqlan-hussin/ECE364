def getUserPermissions():
    D1 = {}
    D2 = {}
    D3 = {}
    L1 = []
    key1 = 0
    j = 0
    with open('AccessCards.txt', 'r') as file1:
        line1 = file1.readlines()

    for i in line1:
        if j > 1 and j < len(line1) - 1:
            temp = i.split('|')
            key = temp[0].strip()
            val = temp[1].strip()
            D1[key] = val
            D2[val] = 0
            j += 1
        else:
            j += 1

    with open('Permissions.txt', 'r') as file2:
        line2 = file2.readlines()

    j = 0
    for i in line2:
        if j > 1:
            temp = i.split()
            key = temp[0]
            val = temp[2]
            if key == key1:
                L1.append(val)
            else:
                j = 2
                L1.clear()
            key1 = key
            if j == 2:
                L1.append(val)
            else:
                L1.sort()
                D2[key] = set(L1)
            j += 1
        else:
            j += 1

    for k1,v1 in D1.items():
        for k2,v2 in D2.items():
            if v1 == k2:
                D3[k1] = v2

    return D3


def getFloorPermissions():
    D1 = getUserPermissions()
    D2 = {}
    L1 = []
    with open('Permissions.txt', 'r') as file2:
        line2 = file2.readlines()
    j = 0
    for i in line2:
        if j > 1:
            temp = i.split()
            key = temp[0]
            val = temp[2]
            L1.append(val)
        else:
            j += 1
    floor = set(L1)
    L1.clear()
    for items in floor:
        for k1,v1 in D1.items():
            for i in v1:
                if items == i:
                    L1.append(k1)
        L1.sort()
        D2[items] = sorted(set(L1))
        L1.clear()

    return D2


def getFloorRooms():
    D1 = {}
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    L7 = []
    L8 = []
    L9 = []
    L10 = []
    with open('AccessLog.txt', 'r') as file2:
        line2 = file2.readlines()
    j = 0
    for i in line2:
        temp = i.split('-')
        key = temp[5].strip()
        val = temp[6].strip()
        if key == 'Recycle':
            L1.append(val)
            L1.sort()
            D1[key] = set(L1)
        if key == 'Research':
            L2.append(val)
            L2.sort()
            D1[key] = set(L2)
        if key == 'Basement':
            L3.append(val)
            L3.sort()
            D1[key] = set(L3)
        if key == 'Equipments':
            L4.append(val)
            L4.sort()
            D1[key] = set(L4)
        if key == 'Archive':
            L5.append(val)
            L5.sort()
            D1[key] = set(L5)
        if key == 'Servers':
            L6.append(val)
            L6.sort()
            D1[key] = set(L6)
        if key == 'Management':
            L7.append(val)
            L7.sort()
            D1[key] = set(L7)
        if key == 'Development':
            L8.append(val)
            L8.sort()
            D1[key] = set(L8)
        if key == 'Chemicals':
            L9.append(val)
            L9.sort()
            D1[key] = set(L9)
        if key == 'Customers':
            L10.append(val)
            L10.sort()
            D1[key] = set(L10)
    return D1


def isAccessGrantedFor(userName, attempt):
    D1 = getFloorPermissions()
    perm = False
    for k1,v1 in D1.items():
        if k1 == attempt[0]:
            for items in v1:
                if items == userName:
                    perm = True
    return perm


def checkAttempts():
    with open('AccessLog.txt', 'r') as file2:
        line2 = file2.readlines()
    D1 = {}
    j = 0
    with open('AccessCards.txt', 'r') as file1:
        line1 = file1.readlines()

    for i in line1:
        if j > 1 and j < len(line1) - 1:
            temp = i.split('|')
            key = temp[0].strip()
            val = temp[1].strip()
            D1[key] = val
            j += 1
        else:
            j += 1

    D2 = getUserPermissions()
    L1 = []
    L2 = []

    for i in line2:
        temp = i.split()
        ID = temp[0]
        temp = temp[2].split('-')
        floor = temp[0]
        room = temp[1]
        for k1,v1 in D1.items():
            if v1 == ID:
                name = k1
                L2.append(name)
                L2.append(floor)
                L2.append(room)
                for k2,v2 in D2.items():
                    if k2 == name:
                        perm = floor in v2
                L2.append(perm)
        L3 = tuple(L2)
        L1.append(L3)
        L2.clear()

    return L1


def getAttemptsOf(userName):
    T1 = checkAttempts()
    L1 = []
    for items in T1:
        if items[0] == userName:
            floor = items[1]
            room = items[2]
            perm = items[3]
            T2 = (floor, room, perm)
            L1.append(T2)
    return sorted(L1)


def getUserAttemptSummary():
    D1 = getUserPermissions()
    D2 = {}
    for k1 in D1.keys():
        L1 = getAttemptsOf(k1)
        granted = 0
        denied = 0
        for items in L1:
            if items[2] == True:
                granted += 1
            else:
                denied += 1
        D2[k1] = (granted,denied)
    return D2


def getFloorAttemptSummary():
    D1 = getFloorPermissions()
    D2 = getUserPermissions()
    D3 = {}
    for k1 in D1.keys():
        D3[k1] = [0,0]
    for k1,v1 in D3.items():
        for k2 in D2.keys():
            L1 = getAttemptsOf(k2)
            for items in L1:
                if items[0] == k1:
                    if items[2] == True:
                        v1[0] += 1
                    else:
                        v1[1] += 1
    D4 = {}
    for k3,v3 in D3.items():
        D4[k3] = (v3[0],v3[1])

    return D4


def getRoomAttemptSummary():
    pass


if __name__ == "__main__":
    a = getUserPermissions()
    print(a)
    b = getFloorPermissions()
    print(b)
    c = getFloorRooms()
    print(c)
    d = checkAttempts()
    print(d)
    e = isAccessGrantedFor('Rivera, Patricia', ('Servers', 'Room46'))
    print(e)
    f = isAccessGrantedFor('Reed, Bobby', ('Equipments', 'Room86'))
    print(f)
    g = getAttemptsOf("Gray, Tammy")
    print(g)
    h = getUserAttemptSummary()
    print(h)
    i = getFloorAttemptSummary()
    print(i)
