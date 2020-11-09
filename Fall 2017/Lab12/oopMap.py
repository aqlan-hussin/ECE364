#! /usr/local/bin/python3.4

class Entry:

    def __init__(self, k=0, v=""):
        if isinstance(k,int) == False:
            raise TypeError("Error: The key should be an int instance.")
        if isinstance(v,str) == False:
            raise TypeError("Error: The value should be a str instance.")
        self.key = k
        self.value = v

    def __str__(self):
        return '({0}: "{1}")'.format(self.key,self.value)

    def __hash__(self):
        t = (self.key, self.value)
        return hash(t)

class Lookup:

    def __init__(self, name):
        if name == "":
            raise ValueError("Error: Name cannot be empty.")
        self._entrySet = []
        self._name = name

    def __str__(self):
        return '["{0}": {1:02d} Entries]'.format(self._name,len(self._entrySet))

    def addEntry(self, entry):
        if entry in self._entrySet:
            raise ValueError("Error: Entry is already in backing store.")
        self._entrySet.append(entry)

    def removeEntry(self, entry):
        if entry not in self._entrySet:
            raise KeyError("Error: Entry is not in backing store.")
        self._entrySet.remove(entry)

    def getEntry(self, key):
        keyList = []
        for items in self._entrySet:
            keyList.append(items.key)
        if key not in keyList:
            raise KeyError("Error: No entry with the given key exists.")
        for items in self._entrySet:
            if items.key == key:
                return items

    def getAsDictionary(self):
        dict = {}
        for items in self._entrySet:
            dict[items.key] = items.value
        return dict

if __name__ == "__main__":
    a = Entry(42,"Answer to Life, the Universe, and Everything")
    print(a)
    b = Lookup("Products")
    b.addEntry(a)
    print(b)
    b.removeEntry(a)
    print(b)
    b.addEntry(a)
    print(b.getEntry(42))
    c = Entry(37,"Hello, World")
    b.addEntry(c)
    print(b.getAsDictionary())
    b.removeEntry(a)
    b.removeEntry(c)
    print(b.getAsDictionary())