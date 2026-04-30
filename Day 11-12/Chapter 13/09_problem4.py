# Write a program to find the maximum of the numbers in a list using the reduce function. 

from functools import reduce

l = [1,353,343,22,5452,3434,23,234,322,2,43,434,4,34]

def max(a,b):
    if(a>b):
        return a
    return b


print(reduce(max,l))
