# Write a program which finds out whether a given name is present in a list or not. 

list=["shafkat", "abul", "babul", "cabul", "kabul", "dabul"]

a=input("Search Name:\t").lower()

if(a in list):
    print("The Guest is in the list")
else:
    print("The Guest is not in the list")