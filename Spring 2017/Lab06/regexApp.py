#! /usr/bin/env python3.4
import re
from uuid import UUID

def loadFile():

    with open("CompanyEmployees.txt", "r") as aFile:
        lines = aFile.readlines()

    return lines

def formatName(First, Last):
    return First + " " + Last

def formatPhoneNumber(n):
    if "-" in n:
        nums = [d for d in str(n)]
        num = []
        for items in nums:
            if items != "-":
                num.append(items)
    else:
        num = [int(d) for d in str(n)]
    i = 0
    str1 = "("
    for items in num:
        if i == 3:
            str1 = str1 + ") " + str(items)
        elif i == 6:
            str1 = str1 + "-" + str(items)
        else:
            str1 += str(items)
        i += 1
    return str1

def getRejectedEntries():
    lines = loadFile()
    L1 = []
    L2 = []
    i = 0
    for items in lines:
        temp1 = re.findall(r"[a-zA-z0-9]+",items)
        if len(temp1) == 2:
            items = items.strip()
            temp2 = re.findall(r"[^,;]+",items)
            temp2 = [temp2[0], temp2[1]]
            if " " in temp2:
                L1.append(temp2[0])
            else:
                temp3 = formatName(temp2[1].strip(),temp2[0])
                L1.append(temp3)
    return sorted(L1)

def getCompleteEntries():
    D1 = {}
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"(\w{8}[-]?\w{4}[-]?\w{4}[-]?\w{4}[-]?\w{12})",items)
        temp2 = re.findall(r"([(]?[0-9]{3}[)-]? ?[0-9]{3}[-]?[0-9]{4})",items)
        temp3 = re.findall(r"(\w+ ?\w+?$)",items)
        if len(temp1) != 0 and len(temp2) != 0 and len(temp3) != 0:
            myID = str(UUID(temp1[0]))
            if "(" in temp2[0]:
                myPN = temp2[0]
            else:
                myPN = formatPhoneNumber(temp2[0])
            state = temp3[0]
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            L1 = [myID, myPN, state]
            D1[name] = L1
    return D1


def getEmployeesWithIDs():
    D1 = {}
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"(\w{8}[-]?\w{4}[-]?\w{4}[-]?\w{4}[-]?\w{12})",items)
        if len(temp1) != 0:
            myID = str(UUID(temp1[0]))
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            D1[name] = myID
    return D1

def getEmployeesWithPhones():
    D1 = {}
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"([(]?[0-9]{3}[)-]? ?[0-9]{3}[-]?[0-9]{4})",items)
        if len(temp1) != 0:
            if "(" in temp1[0]:
                myPN = temp1[0]
            else:
                myPN = formatPhoneNumber(temp1[0])
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            D1[name] = myPN
    return D1


def getEmployeesWithStates():
    D1 = {}
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"(\w+ ?\w+?$)",items)
        if len(temp1) != 0:
            state = temp1[0]
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            D1[name] = state
    return D1


def getEmployeesWithoutIDs():
    L1 = []
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"(\w{8}[-]?\w{4}[-]?\w{4}[-]?\w{4}[-]?\w{12})",items)
        if len(temp1) == 0:
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            L1.append(name)
    L2 = getRejectedEntries()
    L3 = []
    for items in L1:
        if items not in L2:
            L3.append(items)
    return sorted(L3)


def getEmployeesWithoutPhones():
    L1 = []
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"([(]?[0-9]{3}[)-]? ?[0-9]{3}[-]?[0-9]{4})",items)
        if len(temp1) == 0:
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            L1.append(name)
    L2 = getRejectedEntries()
    L3 = []
    for items in L1:
        if items not in L2:
            L3.append(items)
    return sorted(L3)


def getEmployeesWithoutStates():
    L1 = []
    lines = loadFile()
    for items in lines:
        temp1 = re.findall(r"(\w+ ?\w+?$)",items)
        if len(temp1) == 0:
            temp2 = re.findall(r"(\w+[,]? \w+,,)",items)
            temp3 = re.findall(r"(\w+[,]? \w+)",temp2[0])
            if "," in temp3[0]:
                temp4 = re.findall(r"[^, ]+",temp3[0])
                name = formatName(temp4[1],temp4[0])
            else:
                name = temp3[0]
            L1.append(name)
    L2 = getRejectedEntries()
    L3 = []
    for items in L1:
        if items not in L2:
            L3.append(items)
    return sorted(L3)

if __name__ == "__main__":
    a = getRejectedEntries()
    print(a)
    b = getEmployeesWithPhones()
    print(len(b))
    c = getEmployeesWithIDs()
    print(len(c))
    d = getEmployeesWithStates()
    print(len(d))
    e = getEmployeesWithoutIDs()
    print(len(e))
    f = getEmployeesWithoutPhones()
    print(len(f))
    g = getEmployeesWithoutStates()
    print(len(g))
    h = getCompleteEntries()
    print(len(h))