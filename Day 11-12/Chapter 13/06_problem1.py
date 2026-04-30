# Write a program to input name, marks and phone number of a student and format it 
# using the format function like below: 
# "The name of the student is NAME, his marks are MARKS and phone number is PHONE NO." 

name = str(input("Enter your Name:"))
marks = int(input("Enter your marks:"))
phone = int(input("Enter your phone number:"))

s = "The name of the student is {}, his marks are {} and phone number is {}.".format(name,marks,phone)

print(str(s))