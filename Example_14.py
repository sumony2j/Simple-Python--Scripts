#!/usr/bin/python3

# Check If A Character Is Vowel Or Not


def vowel(c):
    if c in ('a','e','i','o','u','A','E','I','O','U'):
        print("Vowel")
    else:
        print("Not Vowel")

n=input('Enter a char:')
vowel(n)