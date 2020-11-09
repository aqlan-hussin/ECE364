#! /usr/local/bin/python3.4
import os

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    return lines

def getRegistration():
    classList = os.listdir("Classes")
    dict = {}
    for items in classList:
        lines = loadFile("Classes/"+items)
        className = items.split(".txt")[0]
        for line in lines:
            name = line.strip()
            if name not in dict.keys():
                dict[name] = [className]
            else:
                list = dict.get(name)
                list.append(className)
                dict[name] = list

    return dict

def getCommonClasses(studentName1, studentName2):
    dict = getRegistration()
    if studentName1 not in dict.keys():
        return None
    if studentName2 not in dict.keys():
        return None
    commonList = []
    list1 = []
    list2 = []
    for k,v in dict.items():
        if k == studentName1:
            list1 = v
        elif k == studentName2:
            list2 = v
    for items in list1:
        if items in list2:
            commonList.append(items)

    return set(commonList)

if __name__ == "__main__":
    print(getRegistration())
    a = getCommonClasses('Merideth Kind', 'Melba Gist')
    print(a)