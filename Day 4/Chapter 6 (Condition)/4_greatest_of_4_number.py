num1=int(input("Enter 1st Integer:"))
num2=int(input("Enter 2nd Integer:"))
if(num1>num2):
    a=num1
else:
    a=num2
num3=int(input("Enter 3rd Integer:"))
if(num3>a):
    a=num3
num4=int(input("Enter 4th Integer:"))
if(num4>a):
    a=num4

print("Greatest number is: ",a)