#! /usr/bin/env python3.4

def getHeadAverage(l, n):
	a = l[:n]
	avg = sum(a)/len(a)
	return avg

def getTailMax(l, m):
	b = l[m:]
	x = max(b)
	return x

def getNumberAverage(l):
	a = []	
	for item in l:
		if isinstance(item,int):
			a.append(item)
	avg = sum(a)/len(a)
	return avg

def getFormattedSSN(n):
	a = [int(d) for d in str(n)]
	length = len(a)
	i = 0
	while i < 9-length:
		a.insert(0,0)
		i = i+1
	a.insert(3,'-')
	a.insert(6,'-')
	str1 = ''.join(str(e) for e in a)
	return str1

def findName(l, s):
	match = [x for x in l if s in x]
	return match[0]

def getColumnSum(mat):
	list = []
	for items in mat:
		list.append(sum(items))
	return list

def getFormattedNames(ln):
	str1 = ln[2] + ", " + ln[0] + " " + ln[1] + "."
	return str1

def getElementwiseSum(l1, l2):
	length = [len(l1), len(l2)]
	l3 = []
	i = 0
	x = min(length)
	y = max(length)
	if length[0] > length[1]:
		n = 1
	else:
		n = 2
	while i < x:
		new = l1[i] + l2[i]
		l3.append(new)
		i = i + 1
	while i < y:
		if n == 1:		
			l3.append(l1[i])
		else:
			l3.append(l2[i])
		i = i + 1
	return l3

def removeDuplicates(l):
	a = []
	for i in l:
		if i not in a:
			a.append(i)
	return a

def getMaxOccurrence(l):
	a = removeDuplicates(l)
	b = []
	for i in a:
		o = 0		
		for j in l:
			if j == i:
				o = o + 1
		b.append(o)
	x = b.index(max(b))
	y = a[x]
	return y

def getMaxProduct(l):
	length = len(l)
	i = 0
	product = []
	while i < length - 2:
		x = l[i] * l[i+1] * l[i+2]		
		product.append(x)
		i = i + 1
	m = max(product)
	return m 	

if __name__ == "__main__":
	l1 = [12, 25, 3, 64, 15]
	l2 = ['A', 2, 'Q', 7, 10, 'L']
	l3 = ["Geoge Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
	l4 = [1, 3, 5, 7, 9, 11]
	l5 = [6, 4, 2]
	l6 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
	l7 = [3, 7, -2, 2, 3, 5]
	mat = [l4, l5]
	n = 1657649
	a = getHeadAverage(l1, 3)
	ln = ["George", "W", "Bush"]
	print ('{}'.format(a))
	b =  getTailMax(l1, 3)
	print ('{}'.format(b))
	c = getNumberAverage(l2)
	print ('{}'.format(c))
	d = getFormattedSSN(n)
	print ('{}'.format(d))
	e = findName(l3,"Johnson")
	print ('{}'.format(e))
	f = getColumnSum(mat)
	print ('{}'.format(f))
	g = getFormattedNames(ln)
	print ('{}'.format(g))
	h = getElementwiseSum(l4,l5)
	print ('{}'.format(h))
	i = removeDuplicates(l6)
	print ('{}'.format(i))
	j = getMaxOccurrence(l6)
	print ('{}'.format(j))
	j = getMaxProduct(l7)
	print ('{}'.format(j))
