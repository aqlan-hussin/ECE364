#! /usr/bin/env python3.4

from points import *
from prelab08addon import performProcessing

def createPoint(dataString):
    p = PointND(0.0)
    L1 = dataString.split(",")
    L2 = []
    msg = "ERROR: String contains non-float values."
    for items in L1:
        try:
            P1 = float(items)
            L2.append(P1)
        except ValueError:
            return msg
    p.n = len(L2)
    p.t = tuple(L2)
    return p

def distanceBetween(point1,point2):
    try:
        dist = point1.distanceFrom(point2)
    except ValueError:
        return "ERROR: Cannot calculate distance"
    return dist

def checkVicinity(point,pointList,radius):
    le = 0
    gt = 0
    nv = 0
    for p in pointList:
        try:
            dist = point.distanceFrom(p)
            if dist <= radius:
                le += 1
            else:
                gt += 1
        except:
            nv += 1
    l = [le,gt,nv]
    return tuple(l)

def checkOperation(*args):
    try:
        performProcessing(args)
        return True
    except ConnectionRefusedError:
        raise
    except OSError as e:
        return "The following Error occured: {0}".format(e.__class__.__name__)
    except:
        return False


if __name__ == "__main__":
    a = createPoint("3.14,19.77")
    b = createPoint("2.0, 4.2")
    print((a))
    print((b))
    c = distanceBetween(a,b)
    print(c)
    d = createPoint("8.7,9.1,7.0")
    r = 5.0
    e = createPoint("5.3,12.9")
    l = [a,b,d,e]
    f = checkVicinity(e,l,r)
    print(f)
    g = checkOperation(a)
    print(g)