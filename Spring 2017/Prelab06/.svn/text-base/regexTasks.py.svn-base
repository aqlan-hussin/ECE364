#! /usr/bin/env python3.4

def getWords(sentence, letter):
    import re
    word1 = re.findall(r"\bT\w+", sentence)
    word2 = re.findall(r"\b\w+t\b", sentence)
    words = word1 + word2
    return words

def extractFloats(s):
    import re
    words = re.findall(r"\d+\.\d+",s)
    return words

def getUrlParts(url):
    import re
    addr = re.findall(r"([^/]+)", url)
    action = re.findall(r"\b\w+?\b", addr[3])
    myList = [addr[1], addr[2], action[0]]
    return tuple(myList)

def getQueryParameters(url):
    import re
    addr = re.findall(r"([^?]+)", url)
    query = re.findall(r"([^&]+)", addr[1])
    myList = []
    for items in query:
        L1 = re.findall(r"([^=]+)", items)
        myList.append(tuple(L1))
    return myList

def findFunctions(fileName):
    with open(fileName) as file1:
        lines = file1.readlines()
    Flines = []
    import re
    for items in lines:
        if "def" in items:
            items = items.strip()
            Flines.append(items)
    L1 = []
    L3 = []
    for items in Flines:
        temp = re.findall(r"([^()]+)",items)
        funcName = temp[0].split()
        L1.append(funcName[1])
        param = re.findall(r"([^, ]+)",temp[1])
        i = 0
        while i < len(param):
            if param[i] == ':':
                param = []
            i += 1
        L1.append(param)
        L3.append(tuple(L1))
        L1.clear()
    return L3

if __name__ == "__main__":
    s1 = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    a = getWords(s1, "t")
    print(a)
    s2 = "The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each."
    b = extractFloats(s2)
    print(b)
    url1 = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    url2 = "http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here"
    c = getUrlParts(url1)
    print(c)
    d = getQueryParameters(url2)
    print(d)
    e = findFunctions("dataStructs.py")
    print(e)