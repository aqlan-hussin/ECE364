#! /usr/local/bin/python3.4


def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()
    return lines

def getStudentInfo():
    returnDict = {}
    lines = loadFile("university.txt")
    i = 0
    for items in lines:
        i += 1
        if i == 2:
            courses = items.split()
            courses.remove("Full")
            courses.remove("Name")
        elif i != 1 and i != 3:
            students = items.split('|')
            name = students[0].strip()
            scores = []
            for j in range(len(students)-1):
                scores.append(students[j+1].strip())
            keyList = []
            for k in range(len(courses)):
                if scores[k] != "-":
                    key = (courses[k],float(scores[k]))
                    keyList.append(key)
            returnDict[name] = keyList

    return returnDict

def getClassInfo():
    returnDict = {}
    studentDict = {}
    courses = []
    lines = loadFile("university.txt")
    i = 0
    for items in lines:
        i += 1
        if i == 2:
            courses = items.split()
            courses.remove("Full")
            courses.remove("Name")
        elif i != 1 and i != 3:
            students = items.split('|')
            name = students[0].strip()
            scores = []
            for j in range(len(students)-1):
                scores.append(students[j+1].strip())
            studentDict[name] = scores
    for x in range(len(courses)):
        keyList = []
        for k,v in studentDict.items():
            if v[x] != "-":
                key = (k,float(v[x]))
                keyList.append(key)
        returnDict[courses[x]] = keyList

    return returnDict

def getBestInCourse(course):
    dict = getClassInfo()
    scores = dict[course]
    name = ""
    highest = 0
    for items in scores:
        if items[1] > highest:
            highest = items[1]
            name = items[0]
    return (name,highest)

def getCourseAverage(course):
    dict = getClassInfo()
    scores = dict[course]
    total = 0
    for items in scores:
        total += items[1]
    return round(total/len(scores),2)

def getCreditHoursDict():
    lines = loadFile("courses.txt")
    dict = {}
    i = 0
    for items in lines:
        i += 1
        if i != 1 and i != 2:
            elem = items.split()
            dict[elem[0]] = int(elem[1])
    return dict

def getStudentGPA(name):
    dict = getStudentInfo()
    scores = dict[name]
    total = 0
    credit = getCreditHoursDict()
    taken = 0
    for i in range(len(scores)):
        weighted = scores[i][1] * credit[scores[i][0]]
        total += weighted
        taken += credit[scores[i][0]]
    return round(total/taken,2)



if __name__ == "__main__":
    a = getStudentInfo()
    print(a["Sadie Farkas"])
    b = getClassInfo()
    print(len(b['ECE139']))
    print(getBestInCourse("ECE388"))
    print(getCourseAverage("ECE344"))
    print(getStudentGPA("Melba Gist"))