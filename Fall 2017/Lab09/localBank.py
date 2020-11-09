#! /usr/local/bin/python3.4
class Transaction:

    def __init__(self, transtype, value):
        if transtype != 'W' and transtype != 'D':
            raise ValueError("Transaction type can be either W or D only.")
        self.transType = transtype
        self.value = value
        pass

class Person:

    def __init__(self, firstName, lastName):
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        pass

    def __str__(self):
        return self.firstName + " " + self.lastName

class Account:

    def __init__(self, accountID, owner, balance):
        self.accountID = accountID
        self.owner = owner
        self.balance = balance
        self.minValue = 1000.0
        pass

    def __str__(self):
        if self.balance >= 0:
            return self.accountID + ", " + str(self.owner) + ", Balance = $" + str(round(self.balance,2))
        else:
            return self.accountID + ", " + str(self.owner) + ", Balance = ($" + str(round(self.balance,2)) + ")"

    def applyTransaction(self, trans):
        if trans.transType == 'D':
            self.balance = round(self.balance + trans.value, 2)
        else:
            if self.balance - trans.value < self.minValue:
                self.balance = round(self.balance - trans.value - 10.0, 2)
            elif self.balance - trans.value >= 0:
                self.balance = round(self.balance - trans.value, 2)
            else:
                raise ValueError("The transaction is invalid.")
        pass

class Bank:

    def __init__(self):
        self.accounts = {}

    def createAccount(self, firstName, lastName, accountID):
        if accountID in self.accounts.keys():
            return
        owner = Person(firstName, lastName)
        myAcc = Account(accountID, owner, 500.0)
        self.accounts[accountID] = myAcc
        pass

    def applyTransaction(self, accountID, transaction):
        if accountID not in self.accounts.keys():
            return
        for k, v in self.accounts.items():
            if k == accountID:
                v.applyTransaction(transaction)
        pass

if __name__ == "__main__":
    a = Person("John","Smith")
    print(a)
    b = Bank()
    b.createAccount("John", "Smith", "10000-90000")
    print(b.accounts)
    c = Transaction('W',100.00)
    b.applyTransaction("10000-90000",c)
    print(b.accounts["10000-90000"])
