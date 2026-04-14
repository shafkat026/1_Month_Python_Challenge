# Write a program to find out whether a student has passed or failed if it requires  
# a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

num1=int(input("Enter Marks of 1st Exam :"))
num2=int(input("Enter Marks of 2nd Exam :"))
num3=int(input("Enter Marks of 3rd Exam :"))

a=(num1+num2+num3)/3

if(num1 >= 33 and num2 >= 33 and num3 >= 33 and a >= 40):
    print("Passed")
else:
    print("Failed, Try again next year.")