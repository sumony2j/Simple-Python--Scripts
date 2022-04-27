#!/usr/bin/python3

# Print The Numbers Which Are lesser Than 5

# Input a list of numbers
l=list(map(float,input("Enter numbers:").strip().split()))
new_l=[i for i in l if i<5] # Create comprehension list of integers whose value is less than 5 from the input list 
print("Output:",end=" ")
print(new_l) # Print Output

