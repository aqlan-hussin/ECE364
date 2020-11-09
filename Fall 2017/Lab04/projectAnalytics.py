#! /usr/local/bin/python3.4

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    return lines

def getStudentIDs():
    lines = loadFile("students.txt")
    dict = {}
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split('|')
            dict[v[0].strip()] = v[1].strip()
        else:
            i += 1
    return dict

def getAllProjectIDs():
    lines = loadFile("projects.txt")
    list = []
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            if v[1] not in list:
                list.append(v[1])
        else:
            i += 1
    return list

def getAllCircuitsbyProjectID(projectID):
    lines = loadFile("projects.txt")
    list = []
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            if v[1] == projectID:
                list.append(v[0])
        else:
            i += 1
    return list

def getProjectIDbyCircuits(circuit):
    lines = loadFile("projects.txt")
    list = []
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            if v[0] == circuit:
                list.append(v[1])
        else:
            i += 1
    return list

def getAllCircuits():
    lines = loadFile("projects.txt")
    list = []
    i = 0
    for items in lines:
        if i != 0 and i != 1:
            v = items.split()
            list.append(v[0])
        else:
            i += 1
    return list

def getComponentCountByProject(projectID):
    if projectID not in getAllProjectIDs():
        return None
    circuits = getAllCircuitsbyProjectID(projectID)

    r = 0
    l = 0
    c = 0
    t = 0
    compList = []
    for cir in circuits:
        filename = "Circuits/circuit_" + str(cir) + ".txt"
        lines = loadFile(filename)
        j = 0
        for items in lines:
            if j != 4:
                j += 1
            else:
                comp = items.split(", ")

        for items in comp:
            compList.append(items)
    for com in set(compList):
        if 'R' in com:
            r += 1
        elif 'L' in com:
            l += 1
        elif 'C' in com:
            c += 1
        elif 'T' in com:
            t += 1
    return (r,l,c,t)

def getComponentCountByStudent(studentName):
    if studentName not in getStudentIDs().keys():
        return None
    studentID = getStudentIDs().get(studentName)
    circuits = getAllCircuits()
    r = 0
    l = 0
    c = 0
    t = 0
    compList = []
    for cir in circuits:
        filename = "Circuits/circuit_" + str(cir) + ".txt"
        #filename = "Circuits/circuit_15565" + ".txt"
        lines = loadFile(filename)
        j = 0
        i = 0
        for items in lines:
            if i == 1:
                participants = items.split(", ")
                participants[len(participants)-1] = participants[len(participants)-1].strip()
            i += 1
        comp = []
        for line in lines:
            if studentID in participants:
                if j != 4:
                    j += 1
                else:
                    comp = line.split(", ")
        #print(comp)
        for items in comp:
            compList.append(items)
    for com in set(compList):
        if 'R' in com:
            r += 1
        elif 'L' in com:
            l += 1
        elif 'C' in com:
            c += 1
        elif 'T' in com:
            t += 1

    if r == 0 and l == 0 and c == 0 and t == 0:
        return ()
    else:
        return (r,l,c,t)

def getParticipationByStudent(studentName):
    if studentName not in getStudentIDs().keys():
        return None
    studentID = getStudentIDs().get(studentName)
    circuits = getAllCircuits()
    cirList = []
    for cir in circuits:
        filename = "Circuits/circuit_" + str(cir) + ".txt"
        #filename = "Circuits/circuit_15565" + ".txt"
        lines = loadFile(filename)
        participants = []
        i = 0
        for items in lines:
            if i == 1:
                participants = items.split(", ")
                participants[len(participants)-1] = participants[len(participants)-1].strip()
            i += 1
        comp = []
        for line in lines:
            if studentID in participants:
                cirList.append(cir)
    proList = []
    for items in cirList:
        projectID = getProjectIDbyCircuits(items)
        for project in projectID:
            if project not in proList:
                proList.append(project)

    return set(proList)

def getParticipationByProject(projectID):
    if projectID not in getAllProjectIDs():
        return None
    circuits = getAllCircuitsbyProjectID(projectID)
    studentList = []
    for cir in circuits:
        filename = "Circuits/circuit_" + str(cir) + ".txt"
        lines = loadFile(filename)
        i = 0
        participants = []
        for items in lines:
            if i == 1:
                participants = items.split(", ")
                participants[len(participants)-1] = participants[len(participants)-1].strip()
            i += 1
        for studentID in participants:
            studentDict = getStudentIDs()
            for k,v in studentDict.items():
                if studentID == v and k not in studentList:
                    studentList.append(k)
    return set(studentList)

def getProjectByComponent(components):
    circuits = getAllCircuits()
    cirList = []
    dict = {}
    for component in components:
        for cir in circuits:
            filename = "Circuits/circuit_" + str(cir) + ".txt"
            lines = loadFile(filename)
            j = 0
            for items in lines:
                if j != 4:
                    j += 1
                else:
                    comp = items.split(", ")
            if component in comp:
                cirList.append(cir)
        projectList = []
        for items in cirList:
            projectID = getProjectIDbyCircuits(items)
            for project in projectID:
                if projectID not in projectList:
                    projectList.append(project)
        dict[component] = projectList

    return dict

def getStudentByComponent(components):
    circuits = getAllCircuits()

    dict = {}
    studentDict = getStudentIDs()
    for component in components:
        studentList = []
        for cir in circuits:
            filename = "Circuits/circuit_" + str(cir) + ".txt"
            lines = loadFile(filename)
            j = 0
            comp = []
            for items in lines:
                if j != 4:
                    j += 1
                else:
                    comp = items.split(", ")
            if component in comp:
                i = 0
                participants = []
                for items in lines:
                    if i == 1:
                        participants = items.split(", ")
                        participants[len(participants)-1] = participants[len(participants)-1].strip()
                    i += 1
                for studentID in participants:
                    for k,v in studentDict.items():
                        if studentID == v and k not in studentList:
                            studentList.append(k)
                dict[component] = studentList

    return dict

def getComponentByStudent(studentNames):
    dict = {}
    for studentName in studentNames:
        studentID = getStudentIDs().get(studentName)
        circuits = getAllCircuits()

        compList = []
        for cir in circuits:
            filename = "Circuits/circuit_" + str(cir) + ".txt"
            lines = loadFile(filename)
            j = 0
            i = 0
            participants = []
            for items in lines:
                if i == 1:
                    participants = items.split(", ")
                    participants[len(participants)-1] = participants[len(participants)-1].strip()
                i += 1
            comp = []
            for line in lines:
                if studentID in participants:
                    if j != 4:
                        j += 1
                    else:
                        comp = line.split(", ")
            for items in comp:
                if items not in compList:
                    compList.append(items)
        dict[studentName] = compList
    return dict

def getCommonByProject(projectID1, projectID2):
    if projectID1 not in getAllProjectIDs():
        return None
    if projectID2 not in getAllProjectIDs():
        return None
    commonList = []
    circuits1 = getAllCircuitsbyProjectID(projectID1)
    circuits2 = getAllCircuitsbyProjectID(projectID2)
    components1 = []
    components2 = []
    for cir in circuits1:
        filename = "Circuits/circuit_" + str(cir) + ".txt"
        lines = loadFile(filename)
        i = 0
        for items in lines:
            if i == 4:
                component1 = items.split(", ")
            i += 1
        for items in component1:
            components1.append(items)
    for cir in circuits2:
        filename = "Circuits/circuit_" + str(cir) + ".txt"
        lines = loadFile(filename)
        i = 0
        for items in lines:
            if i == 4:
                component2 = items.split(", ")
            i += 1
        for items in component2:
            components2.append(items)
    for item1 in components1:
        for item2 in components2:
            if item1 == item2 and item1 not in commonList:
                commonList.append(item1)

    return sorted(commonList)

def getCommonByStudent(studentName1, studentName2):
    if studentName1 not in getStudentIDs().keys():
        return None
    if studentName2 not in getStudentIDs().keys():
        return None
    commonList = []
    components1 = getComponentByStudent([studentName1])
    components2 = getComponentByStudent([studentName2])
    for item1 in components1.values():
        for comp1 in item1:
            for item2 in components2.values():
                for comp2 in item2:
                    if comp1 == comp2 and comp1 not in commonList:
                        commonList.append(comp1)

    return sorted(commonList)

def getProjectByCircuit():
    circuits = getAllCircuits()
    dict = {}
    for circuit in circuits:
        projectID = getProjectIDbyCircuits(circuit)
        dict[circuit] = sorted(set(projectID))
    return dict

def getCircuitByStudent():
    students = getStudentIDs()
    dict = {}
    for k,v in students.items():
        circuits = getAllCircuits()
        cirList = []
        for cir in circuits:
            filename = "Circuits/circuit_" + str(cir) + ".txt"
            lines = loadFile(filename)
            i = 0
            participants = []
            for items in lines:
                if i == 1:
                    participants = items.split(", ")
                    participants[len(participants)-1] = participants[len(participants)-1].strip()
                i += 1
            if v in participants:
                cirList.append(cir)
        dict[k] = sorted(set(cirList))
    return dict

def getCircuitByStudentPartial(studentName):
    students = getStudentIDs()
    flag = False
    studentNames = []
    for items in students.keys():
        if studentName in items:
            flag = True
            studentNames.append(items)
    if flag == False:
        return None
    dict = {}
    for student in studentNames:
        for k,v in students.items():
            circuits = getAllCircuits()
            cirList = []
            for cir in circuits:
                filename = "Circuits/circuit_" + str(cir) + ".txt"
                lines = loadFile(filename)
                i = 0
                participants = []
                for items in lines:
                    if i == 1:
                        participants = items.split(", ")
                        participants[len(participants)-1] = participants[len(participants)-1].strip()
                    i += 1
                if k == student:
                    cirList.append(cir)
                    dict[k] = sorted(set(cirList))
    return dict


if __name__ == "__main__":
    #print(len(getAllProjectIDs()))
    a = getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    print(a)
    b = getComponentCountByStudent("Alexander, Carlos")
    print(b)
    c = getParticipationByStudent("Adams, Keith")
    print(c)
    d = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    print(d)
    e = getProjectByComponent({"R726.432"})
    print(e)
    f = getStudentByComponent({"R726.432"})
    print(f)
    g = getComponentByStudent({"Brown, Robert"})
    print(len(g.get("Brown, Robert")))
    h = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6","83383848-1D69-40D4-A360-817FB22769ED")
    print(h)
    i = getCommonByStudent('Brown, Robert', 'Richardson, George')
    print(i)
    j = getProjectByCircuit()
    print(j)
    #k = getCircuitByStudent()
    #print(k)
    #l = getCircuitByStudentPartial("Brown")
    #print(l)
