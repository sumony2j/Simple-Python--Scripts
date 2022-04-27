#!/usr/bin/python3

# Class Concept Implementation In Python

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def set_details(self):
        self.department=input("Input the department of {}:".format(self.name))
        self.id=int(input("Input the id of {}:".format(self.name)))
        self.grade=int(input("Input the grade of {}:".format(self.name)))
    def display(self):
        print('{} of {} whose id is {} and age is {} scored {} in last sememster'.format(self.name,self.department,self.id,self.age,self.grade))

class B(A):
    def __init__(self, name, age):
        super().__init__(name, age)
    def display(self):
        return super().display()

S=B('Sumon',22)
S.set_details()
S.display()