#! /usr/bin/env python3.4

def uniqueLetters(s):
	l = set(s)
	a = sorted(l, reverse = True)
	str1 = "\""+''.join(a)+"\""
	return str1

def scaleSet(aSet, num):
	bSet = []
	for i in aSet:
		n = i * num
		n = round(n,2)
		bSet.append(n)
	return set(bSet)

def printNames(aSet):
	l = sorted(aSet)	
	for i in l:
		print ('{}'.format(i))
	return

def getStateName(stateAbb):
	dic = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
	for key, val in dic.items():
		if val == stateAbb:
			return key

def getZipCodes(stateName):
	d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
	d2 = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}
	l = []
	abb = 0
	for key1, val1 in d1.items():
		if key1 == stateName:
			abb = val1
	for key2, val2 in d2.items():
		if val2 == abb:
			l.append(key2)
	return set(l)

def printSortedMap(s):	
	for (lastName, firstName, mi), weight in sorted(s.items()):
    		o = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
    		print(o)
	return

def switchNames(s):
	l = []
	for (lastName, firstName, mi) in sorted(s.keys()):
		first = firstName
		last = lastName
		str1 = first + " " + last
		s[str1] = s.pop((lastName, firstName, mi))
	return s

def getPossibleMatches(record, n):
	l = []	
	for string, (month, day, year) in sorted(record.items()):
		if month == n or day == n or year == n:
			l.append(string)
	return set(l)

def getPurchaseReport():
	D1 = {}
	D3 = {}
	j = 0
	with open('purchases/Item List.txt', 'r') as file1:
		line1 = file1.readlines()
	for i in line1:
		if j == 2:		
			temp = i.split()
			D1[temp[0]] = temp[1]
		else:
			j += 1
	import glob
	import re
	F = glob.glob('purchases/purchase_*')
	ID = []
	tranID = []
	for i in sorted(F):
		ID.append(re.findall('\d+',i))
	for i in ID:
		for k in i:
			tranID.append(k)
	index = 0	
	while index < len(tranID):
		with open (F[index], 'r') as file2:
			line2 = file2.readlines()
		j = 0
		D2 = {}		
		for i in line2:
			if j == 2:		
				temp = i.split()
				D2[temp[0]] = temp[1]
			else:
				j += 1
		cost = 0		
		for key1, val1 in D1.items():
			for key2, val2 in D2.items():
				if key1 == key2:
					price = re.findall('\d+\.\d+',val1)
					cost += float(val2) * float(price[0])
					cost = round(cost,2)
		D3[int(tranID[index])] = cost
		index += 1
	return D3

def getTotalSold():
	D1 = {}
	D3 = {}
	j = 0
	with open('purchases/Item List.txt', 'r') as file1:
		line1 = file1.readlines()
	for i in line1:
		if j == 2:		
			temp = i.split()
			D1[temp[0]] = temp[1]
			D3[temp[0]] = 0
		else:
			j += 1
	import glob
	import re
	F = glob.glob('purchases/purchase_*')
	ID = []
	tranID = []
	for i in sorted(F):
		ID.append(re.findall('\d+',i))
	for i in ID:
		for k in i:
			tranID.append(k)
	index = 0
	while index < len(F):
		with open (F[index], 'r') as file2:
			line2 = file2.readlines()
		j = 0
		D2 = {}		
		for i in line2:
			if j == 2:		
				temp = i.split()
				D2[temp[0]] = temp[1]
			else:
				j += 1		
		for key1, val1 in D3.items():
			for key2, val2 in D2.items():
				if key1 == key2:
					D3[key1] = val1 + int(val2)
		index += 1
	return D3	

if __name__ == "__main__":
	a = uniqueLetters("ABDBDARWET")
	print ('{}'.format(a))
	s = {3.12, 5.0, 7.2, 15.24}
	b = scaleSet(s, 2.1)
	print ('{}'.format(b))
	c = {"Frank","Xavier","L","James"}
	printNames(c)
	d = getStateName("IN")
	print ('{}'.format(d))
	e = getZipCodes("Indiana")
	print ('{}'.format(e))
	f = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
	printSortedMap(f)
	g = switchNames(f)
	print(g)
	record = {"Frank": (3, 6, 95), "Xavier": (3, 24, 93), "James": (9, 1, 95)}
	h = getPossibleMatches(record, 3)
	print(h)
	i = getPurchaseReport()
	print(i)
	j = getTotalSold()
	print(j)
