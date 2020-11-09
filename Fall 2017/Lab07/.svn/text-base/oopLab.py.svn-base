#! /usr/local/bin/python3.4

class Rectangle:

    def __init__(self, llpoint, urpoint):
        if llpoint[0] >= urpoint[0] or llpoint[1] >= urpoint[1]:
            raise ValueError("Lower-Left point must be less than Upper-Right point.")
        self.lowerLeft = llpoint
        self.upperRight = urpoint

    def isSquare(self):
        x = self.upperRight[0] - self.lowerLeft[0]
        y = self.upperRight[1] - self.lowerLeft[1]
        if x == y:
            return True
        else:
            return False

    def isPointInside(self, point):
        if point[0] > self.lowerLeft[0] and point[0] < self.upperRight[0] and point[1] > self.lowerLeft[1] and point[1] < self.upperRight[1]:
            return True
        else:
            return False

    def intersectsWith(self, rect):
        upperLeft = (rect.lowerLeft[0],rect.upperRight[1])
        lowerRight = (rect.upperRight[0],rect.lowerLeft[1])
        if self.isPointInside(rect.lowerLeft) or self.isPointInside(rect.upperRight) or self.isPointInside(upperLeft) or self.isPointInside(lowerRight):
            return True
        else:
            return False


if __name__ == "__main__":
    a = Rectangle((0,0),(2,2))
    print(a.isSquare())
    b = Rectangle((-2,-5),(6,3))
    print(b.isPointInside((0,0)))
    c = Rectangle((-3,-8),(0,0))
    print(b.intersectsWith(c))
    print(c.intersectsWith(b))
    d = Rectangle((1,-1),(3,1))
    print(d.intersectsWith(a))