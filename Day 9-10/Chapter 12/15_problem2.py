# Write a program to print third, fifth and seventh element 
# from a list using enumerate function. 

myList = [1,2,3,4,5,6,7,67,8]


for index, item in enumerate(myList):
    if index == 2 or index == 4 or index == 6:
        print(f"the item number {index} is {item}")

for index, item in enumerate(myList):
    if index in [2, 4, 6]:
        print(f"The item number {index} is {item}")

