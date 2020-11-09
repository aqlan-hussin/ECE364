#! /usr/local/bin/python3.4
import re
from uuid import UUID

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    return lines

def getUrlParts(url):
    part = re.findall(r"([^/]+)",url)
    action = re.findall(r"\b\w+?\b", part[3])
    return (part[1], part[2], action[0])

def getQueryParameters(url):
    part = re.findall(r"([^?]+)",url)
    query = re.findall(r"([^&]+)", part[1])
    qList = []
    for items in query:
        q = re.findall(r"([^=]+)",items)
        qList.append(tuple(q))
    return qList

def getSpecial(sentence, letter):
    start = re.findall(r"\b"+re.escape(letter)+r"\w+",sentence, re.IGNORECASE)
    end = re.findall(r"\w+"+re.escape(letter)+r"\b",sentence, re.IGNORECASE)
    for s in start:
        for e in end:
            if s == e:
                start.remove(s)
                end.remove(e)
    return start + end

def getRealMAC(sentence):
    regex = r"[0-9a-f]{2}[:-][0-9a-f]{2}[:-][0-9a-f]{2}[:-][0-9a-f]{2}[:-][0-9a-f]{2}[:-][0-9a-f]{2}"
    return re.findall(regex,sentence,re.IGNORECASE)

def formatPhoneNumber(num):
    if "(" and ")" in num:
        return  num
    elif "-" in num:
        p = [d for d in str(num)]
        n = []
        for items in p:
            if items != "-":
                n.append(items)
    else:
        n = [int(d) for d in str(num)]
    i = 0
    pn = "("
    for items in n:
        if i == 3:
            pn += ") " + str(items)
        elif i == 6:
            pn += "-" + str(items)
        else:
            pn += str(items)
        i += 1
    return pn

def getRejectedEntries():
    lines = loadFile("Employees.txt")
    i = 0
    entryList = []
    for items in lines:
        part = re.findall(r"[a-zA-Z0-9]+",items)
        if len(part) == 2:
            field = re.findall(r"[^,;]+",items)
            if " " in field[0]:
                name = field[0]
            else:
                name = re.findall(r"\w+",field[1])[0] + " " + field[0]
            entryList.append(name)
    return sorted(entryList)

def EmployeeDict():
    lines = loadFile("Employees.txt")
    dict = {}
    for items in lines:
        name = re.findall(r"(\w+, \w+|\w+ \w+)[,;]",items)
        if "," in name[0]:
            n = re.findall(r"[^,]+",name[0])
            name = re.findall(r"\w+",n[1])[0] + " " + n[0]
        else:
            name = name[0]
        ID = re.findall(r"\w{32}|[\w|-]{36}",items)
        if len(ID) == 1:
            ID = str(UUID(ID[0]))
        else:
            ID = None
        phone = re.findall(r"\d{10}|[\d-]{12}|[\d\(\) -]{14}",items)
        if len(phone) == 1:
            num = formatPhoneNumber(phone[0])
        else:
            num = None
        state = re.findall(r"([\w ]+)$",items)
        if len(state) == 1:
            state = state[0]
        else:
            state = None
        dict[name] = [ID,num,state]
    return dict

def getEmployeesWithIDs():
    dict = EmployeeDict()
    d = {}
    for k,v in dict.items():
        if v[0] != None:
            d[k] = v[0]
    return d

def getEmployeesWithoutIDs():
    dict = EmployeeDict()
    eList = []
    for k,v in dict.items():
        if v[0] == None and (v[1] != None or v[2] != None):
            eList.append(k)
    return sorted(eList)

def getEmployeesWithPhones():
    dict = EmployeeDict()
    d = {}
    for k,v in dict.items():
        if v[1] != None:
            d[k] = v[1]
    return d

def getEmployeesWithStates():
    dict = EmployeeDict()
    d = {}
    for k,v in dict.items():
        if v[2] != None:
            d[k] = v[2]
    return d

def getCompleteEntries():
    dict = EmployeeDict()
    d = {}
    for k,v in dict.items():
        if v[0] != None and v[1] != None and v[2] != None:
            d[k] = (v[0],v[1],v[2])
    return d

if __name__ == "__main__":
    url1 = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    url2 = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    print(getUrlParts(url1))
    print(getQueryParameters(url2))
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getSpecial(s, "t"))
    x = "The MAC addresses are 58:1C:0A:6E:39:4D or 58-1c-0a-6e-39-4d"
    print(getRealMAC(x))
    print(formatPhoneNumber("(765) 637-8530"))
    print(getRejectedEntries())
    print(getEmployeesWithIDs())
    print(getEmployeesWithoutIDs())
    print(getEmployeesWithPhones())
    print(getEmployeesWithStates())
    print(getCompleteEntries())
