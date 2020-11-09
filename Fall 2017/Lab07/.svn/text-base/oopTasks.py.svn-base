#! /usr/local/bin/python3.4
import enum
import re
import random

class Level(enum.Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4

class Student:

    def __init__(self, ID, firstName, lastName, level):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        if type(level) is not Level:
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
        self.level = level

    def __str__(self):
        level = str(self.level.name)
        return str(self.ID) + ", " + str(self.firstName) + " " + str(self.lastName) + ", " + level.capitalize()

class Circuit:

    def __init__(self, ID, r, c, i, t):
        self.ID = ID
        for items in r:
            if not re.match(r'R\d+\.\d+',items):
                raise ValueError("The resistors' list contain invalid components.")
        for items in c:
            if not re.match(r'C\d+\.\d+',items):
                raise ValueError("The capacitors' list contain invalid components.")
        for items in i:
            if not re.match(r'L\d+\.\d+',items):
                raise ValueError("The inductors' list contain invalid components.")
        for items in t:
            if not re.match(r'T\d+\.\d+',items):
                raise ValueError("The transistors' list contain invalid components.")
        self.resistors = r
        self.capacitors = c
        self.inductors = i
        self.transistors = t

    def __str__(self):
        r = len(self.resistors)
        c = len(self.capacitors)
        i = len(self.inductors)
        t = len(self.transistors)
        return str(self.ID) + ": (R = " + "{0:02d}".format(r) + ", C = " + "{0:02d}".format(c) + ", L = " + "{0:02d}".format(i) + ", T = " + "{0:02d}".format(t) + ")"

    def getDetails(self):
        myStr = str(self.ID) + ": "
        for items in self.resistors:
            myStr += items + ", "
        for items in self.capacitors:
            myStr += items + ", "
        for items in self.inductors:
            myStr += items + ", "
        for items in self.transistors:
            myStr += items + ", "
        return myStr[:-2]

    def __contains__(self, item):
        if type(item) is not str:
            raise TypeError("The argument must be an instance of string.")
        if re.match(r'R\d+\.\d+',item):
            return item in self.resistors
        elif re.match(r'C\d+\.\d+',item):
            return item in self.capacitors
        elif re.match(r'L\d+\.\d+',item):
            return item in self.inductors
        elif re.match(r'T\d+\.\d+',item):
            return item in self.transistors
        else:
            raise ValueError("The argument must starts with R, C, L, or T.")

    def __add__(self, other):
        if type(other) is str:
            if other in self:
                return self
            else:
                if re.match(r'R\d+\.\d+',other):
                    self.resistors.append(other)
                elif re.match(r'C\d+\.\d+',other):
                    self.capacitors.append(other)
                elif re.match(r'L\d+\.\d+',other):
                    self.inductors.append(other)
                elif re.match(r'T\d+\.\d+',other):
                    self.transistors.append(other)
                return self
        elif type(other) is Circuit:
            ID = ''.join(random.sample('0123456789',5))
            r = set(self.resistors + other.resistors)
            c = set(self.capacitors + other.capacitors)
            i = set(self.inductors + other.inductors)
            t = set(self.transistors + other.transistors)
            return Circuit(ID,list(r),list(c),list(i),list(t))
        else:
            raise TypeError("__add__ only supports string or Circuit instances")

    def __radd__(self, other):
        if type(other) is not str:
            raise TypeError("__radd__ only supports string instance")
        if other in self:
            return self
        else:
            if re.match(r'R\d+\.\d+',other):
                self.resistors.append(other)
            elif re.match(r'C\d+\.\d+',other):
                self.capacitors.append(other)
            elif re.match(r'L\d+\.\d+',other):
                self.inductors.append(other)
            elif re.match(r'T\d+\.\d+',other):
                self.transistors.append(other)
            return self

    def __sub__(self, other):
        if other not in self:
            return self
        else:
            if re.match(r'R\d+\.\d+',other):
                self.resistors.remove(other)
            elif re.match(r'C\d+\.\d+',other):
                self.capacitors.remove(other)
            elif re.match(r'L\d+\.\d+',other):
                self.inductors.remove(other)
            elif re.match(r'T\d+\.\d+',other):
                self.transistors.remove(other)
            return self

class Project:

    def __init__(self, ID, participants, circuits):
        self.ID = ID
        if len(participants) == 0:
            raise ValueError("Participants' list cannot be empty.")
        if len(circuits) == 0:
            raise ValueError("Circuits' list cannot be empty.")
        for items in participants:
            if type(items) is not Student:
                raise ValueError("Participants' list must be instances of Student")
        for items in circuits:
            if type(items) is not Circuit:
                raise ValueError("Circuits' list must be instances of Circuit")
        self.participants = participants
        self.circuits = circuits

    def __str__(self):
        return self.ID + ": " + "{0:02d}".format(len(self.circuits)) + " Circuits, " + "{0:02d}".format(len(self.participants)) + " Participants"

    def getDetails(self):
        myStr = self.ID + "\n\n" + "Participants:\n"
        for items in self.participants:
            myStr += str(items) + "\n"
        myStr += "\nCircuits:\n"
        for items in self.circuits:
            myStr += items.getDetails() + "\n"
        return myStr[:-1]

    def __contains__(self, item):
        if type(item) is str:
            for circuit in self.circuits:
                if item in circuit:
                    return True
            return False
        elif type(item) is Circuit:
            for circuit in self.circuits:
                if item.ID == circuit.ID:
                    return True
            return False
        elif type(item) is Student:
            for student in self.participants:
                if item.ID == student.ID:
                    return True
            return False
        else:
            raise TypeError("__contains__ only supports string, Circuit or Student instances")

    def __add__(self, other):
        if type(other) is Circuit:
            if other in self.circuits:
                return self
            else:
                self.circuits.append(other)
                return self
        elif type(other) is Student:
            if other in self.participants:
                return self
            else:
                self.participants.append(other)
                return self
        else:
            raise TypeError("__add__ only supports Circuit or Student instances")

    def __sub__(self, other):
        if type(other) is Circuit:
            if other not in self.circuits:
                return self
            else:
                self.circuits.remove(other)
                return self
        elif type(other) is Student:
            if other not in self.participants:
                return self
            else:
                self.participants.remove(other)
                return self
        else:
            raise TypeError("__sub__ only supports Circuit or Student instances")

class Capstone(Project):

    def __init__(self, ID, participants, circuits):
        super(Capstone,self).__init__(ID,participants,circuits)
        for student in participants:
            if student.level is not Level.senior:
                raise ValueError("Participants must be senior level")

    def __add__(self, other):
        if type(other) is Student:
            if other.level is not Level.senior:
                raise ValueError("Participants must be senior level")
        return super(Capstone,self).__add__(other)

if __name__ == "__main__":
    a = Student("15487-79431","John","Smith",Level.freshman)
    print(a)
    b = Circuit("99887",["R555.555","R123.123"],[],[],["T111.111"])
    print(b)
    print(b.getDetails())
    print("T111.111" in b)
    c = Circuit("10101",["R123.123","R176.413"],["C135.246"],[],["T111.111","T222.222"])
    d = Circuit("12345",["R150.150"],[],[],[])
    print(d.getDetails())
    e = d - "R123.122"
    print(e.getDetails())
    f = Project("38753067-e3a8-4c9e-bbde-cd13165fa21e",[a],[b,c])
    print(f)
    #print(f.getDetails())
    print("R555.555" in f)
    g = f + d
    print(g)
    h = g - d
    print(h)
    i = Student("43312-12378","James","Gordon",Level.senior)
    h = h + i
    print(h)
    h = h - a
    print(h)
    j = Capstone("38753067-e3a8-4c9e-bbde-cd13165fa21d",[i],[e])
    print(j)
    k = Student("12343-12340","Jimmy","Neutron",Level.senior)
    j = j + k
    print(j)