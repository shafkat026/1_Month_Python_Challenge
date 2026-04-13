# Q. Write a program to accept marks of 6 students and display them in a sorted manner. 

Marks= []

m1= int(input("Enter Marks:\t"))        #if not "int(input())", then it will short alphabetically
Marks.append(m1)
m2= int(input("Enter Marks:\t"))
Marks.append(m2)
m3= int(input("Enter Marks:\t"))
Marks.append(m3)
m4= int(input("Enter Marks:\t"))
Marks.append(m4)
m5= int(input("Enter Marks:\t"))
Marks.append(m5)
m6= int(input("Enter Marks:\t"))
Marks.append(m6)

Marks.sort()
print(Marks)


# Q. Write a program to sum a list with 6 numbers. 

print(sum(Marks))


# Q. Write a program to count the number of zeros in the following tuple: 

a = (7, 0, 8, 0, 0, 9)

print(a.count(0))