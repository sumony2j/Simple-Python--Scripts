#!/usr/bin/python3

# Implement Histogram In Cli

# Declare function for printing the histogram
def hist(l,Option='Row'): 
    print('Output:')
    if Option == 'Row' or Option=='row': # Row-wise histogram
        for i in l: 
            print("*"*i) 
    elif Option == 'Col' or Option == 'col': # Column-wise histogram
        m=max(l)
        for i in range(0,m):
            for j in range(0,len(l)):
                if i<l[j]:
                    print('*',end=" ")
                else:
                    print(" ",end=" ")
            print('\n')
    else:
        print("Please Enter A Correct Option:")
        print("Type 'Row/row' for row-wise histogram")
        print("Type 'Col/col' for column-wise histogram")
        

# Input a list of integers
a=list(map(int,input("Enter numbers:").strip().split()))
option=input("Enter 'row/Row' for row-wise histogram\nEnter 'col/Col' for column-wise histogram:")
# Call the hist function
hist(a,option)