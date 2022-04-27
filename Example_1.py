#!/usr/bin/python3

# Check If A Number Is Pallindrom/Amstrong Or Not

def ams(n):
    c=0
    for i in str(n):
        c=c+pow(int(i),3)
    if(n==c):
        return True
    False

def pal(n):
    s=str(n)
    if len(s)%2!=0:
        return False
    if(s==s[::1]):
        return True
    else:
        return False
    

n=int(input('Enter a value:'))

if(ams(n)):
    print("Amstrong Number")
else:
    print("Non-Amstrong Number")

if(pal(n)):
    print("Pallindrom Number")
else:
    print("Non-Pallindrom Number")
        