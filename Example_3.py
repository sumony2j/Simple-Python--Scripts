#!/usr/bin/python3

# Class Concept Implementation In Python

class Number:
    MULTIPLIER=5
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def add(self):
        return (self.x+self.y)
    @classmethod
    def multiply(self,a):
        return (self.MULTIPLIER*a)
    @staticmethod
    def subtract(b,c):
        return (b-c)
    @property
    def value(self):
        return (self.x,self.y)
    def setx(self,val):
        self.x=val
    def sety(self,val):
        self.y=val
    def delx(self):
        del self.x
    def dely(self):
        del self.y

A = Number(5,6)
print(A.add())
print(A.multiply(5))
print(A.subtract(9,7))
A.setx(10)
A.sety(30)
print(A.value)
A.delx()
A.dely()