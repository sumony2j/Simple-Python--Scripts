#!/usr/bin/python3

# Implementation Of Fibbonaci Series In Python

def febb(n):
    if n<=1:
        return n
    else:
        return(febb(n-1)+febb(n-2))

n=int(input('Enter a value:'))
for i in range(n):
    print(febb(i))