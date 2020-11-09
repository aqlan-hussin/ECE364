#! /usr/bin/env python3.4

class Duration:

    def __init__(self, weeks, days, hours):
        if type(weeks) is not int:
            raise TypeError("This class only accepts integers")
        if type(days) is not int:
            raise TypeError("This class only accepts integers")
        if type(hours) is not int:
            raise TypeError("This class only accepts integers")
        if weeks < 0:
            raise ValueError("Weeks cannot be negative")
        if days < 0:
            raise ValueError("Days cannot be negative")
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        if hours >= 24:
            addD = hours // 24
            hours = hours % 24
            days = days + addD
        if days >= 7:
            addW = days // 7
            days = days % 7
            weeks = weeks + addW
        self.weeks = weeks
        self.days = days
        self.hours = hours
        pass

    def __str__(self):
        return "{0:02d}W {1:01d}D {2:02d}H".format(self.weeks,self.days,self.hours)

    def getTotalHours(self):
        total = (self.weeks * 7 * 24) + (self.days * 24) + self.hours
        return total

    def __add__(self, other):
        if type(other) is not Duration:
            raise TypeError("Type \"Duration\" is expected")
        newW = self.weeks + other.weeks
        newD = self.days + other.days
        newH = self.hours + other.hours
        new = Duration(newW,newD,newH)
        return new

    def __mul__(self, other):
        if type(other) is not int:
            raise TypeError("Type integer is expected")
        if other <= 0:
            raise ValueError("Value must be greater than 0")
        totalH = self.getTotalHours()
        newH = totalH * other
        new = Duration(0,0,newH)
        return new

if __name__ == "__main__":
    d = Duration(2,15,49)
    print(str(d))
    e = Duration(4,2,76)
    print(str(e))
    f = d + e
    print(str(f))
    g = d * 2
    print(str(g))