#!/usr/bin/python3

# Implement Of Factorial In Python

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return(n*fact(n-1))


n=int(input('Enter a value:'))
f=fact(n)
print(f)