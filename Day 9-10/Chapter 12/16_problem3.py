# Write a list comprehension to print a list which contains 
# the multiplication table of a user entered number

# Store the multiplication tables generated in a file named Tables.txt


table = int(input("Table for: "))

myList = [1,2,3,4,5,6,7,8,9,10]

TableOut1 = [i * table for i in myList]
TableOut = [i * table for i in range(1, 11)]

print(TableOut1)
print(TableOut)

with open("Table.txt", "a") as f:
    f.write(f"Table of {table} is {str(TableOut)} \n")
