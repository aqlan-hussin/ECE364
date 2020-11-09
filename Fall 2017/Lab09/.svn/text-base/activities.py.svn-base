#! /usr/local/bin/python3.4
from localBank import *
import re

def loadFile(filename):
    with open(filename, "r") as myFile:
        lines = myFile.readlines()
    return lines

def loadBankData(dataFileName):
    lines = loadFile(dataFileName)
    i = 0
    b = Bank()
    for items in lines:
        if i == 3:
            fields = items.split('|')
            name = fields[0].strip()
            firstName = name.split()[0]
            lastName = name.split()[1]
            ID = fields[1].strip()
            trans = fields[2].strip()
            b.createAccount(firstName, lastName, ID)
            if '(' in trans:
                val = float(trans.split('$')[1].split(')')[0])
                t = Transaction('W', val)
            else:
                val = float(trans.split('$')[1])
                t = Transaction('D', val)
            try:
                b.applyTransaction(ID, t)
            except:
                reject = 1
        else:
            i += 1
    return b

def getTotalBalanceByPerson(bank, person):
    pass

def getBalances(bank):
    pass

if __name__ == "__main__":
    a = loadBankData("transactions.txt")
    print(a.accounts["44471-18426"])