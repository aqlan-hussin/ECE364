#! /usr/bin/env python3.4
import re
class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        self.experimentNumber = experimentNo
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = unitCount
        self.unitCost = unitCost
        self.totalCost = unitCount * unitCost
        pass

    def __str__(self):
        return str("{0:03d}".format(self.experimentNumber) + ", " + self.experimentDate + ", $" + "{0:06.2f}".format(self.totalCost) + ": " + self.virusName)


class Technician:

    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}
        pass

    def __str__(self):
        num = len(self.experiments)
        return str(self.techID + ", " + self.techName + ": " + "{0:02d} Experiments".format(num))

    def addExperiment(self, experiment):
        num = experiment.experimentNumber
        self.experiments[num] = experiment
        pass

    def getExperiment(self, expNo):
        if expNo in self.experiments.keys():
            return self.experiments[expNo]
        else:
            return None

    def loadExperimentsFromFile(self, fileName):
        with open(fileName) as file1:
            lines = file1.readlines()
        i = 0
        for items in lines:
            if i != 2:
                i += 1
            else:
                info = items.strip()
                info = info.split()
                cost = re.findall(r'[^$]+',info[4])
                exp = Experiment(int(info[0]),info[1],info[2],int(info[3]),float(cost[0]))
                self.experiments[int(info[0])] = exp
        return

    def generateTechActivity(self):
        str1 = self.techID + ", " + self.techName + "\n"
        i = 0
        for k,v in sorted(self.experiments.items()):
            if i == len(self.experiments)-1:
                str1 += v.__str__()
            else:
                str1 += v.__str__() + "\n"
            i += 1
        return str1


class Laboratory:

    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}
        pass

    def __str__(self):
        str1 = self.labName + ": " + "{0:02d} Technicians".format(len(self.technicians)) + "\n"
        i = 0
        res = []
        for k,v in self.technicians.items():
            res.append(str(v))
        res = sorted(res)
        ret_str = "\n".join(res)
        return str1+ret_str

    def addTechnician(self, technician):
        self.technicians[technician.techName] = technician
        pass

    def getTechnicians(self, *args):
        L1 = []
        for items in args:
            L1.append(self.technicians[items])
        return L1

    def generateLabActivity(self):
        str1 = ""
        i = 0
        for k,v in sorted(self.technicians.items()):
            if i == len(self.technicians)-1:
                str1 += v.generateTechActivity()
            else:
                str1 += v.generateTechActivity() + "\n\n"
            i += 1
        return str1

if __name__ == "__main__":
    a = Experiment(31,"04/01/2015","Alphatorquevirus",9,0.50)
    print(a.__str__())
    b = Technician("Irene Adler", "69069-29232")
    b.addExperiment(a)
    c = Experiment(13,"08/14/2015","Hepatovirus",7,2.3)
    b.addExperiment(c)
    b.loadExperimentsFromFile("report 69069-29232.txt")
    print(b.getExperiment(31))
    print(b.generateTechActivity())
    d = Technician("Sherlock Holmes", "55926-36619")
    d.loadExperimentsFromFile("report 55926-36619.txt")
    e = Laboratory("Eli Lilly")
    e.addTechnician(b)
    e.addTechnician(d)
    print(e.__str__())
    print(e.generateLabActivity())