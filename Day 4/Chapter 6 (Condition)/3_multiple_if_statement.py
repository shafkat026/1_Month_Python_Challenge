age= float(input("Enter Your Age:\t"))

#If statement No 1
if(age%2==0):
    print("Age is even")
else:
    print("Age is odd")
#End of If statement No 1

#If statement No 2
if(age>=18):
    print("You are eligible.")
elif(age<0):
    print("Invalid Input.")
elif(age==0):
    print("\"0\" is not a valid age.")
else:
    print("You are not eligible.")
#End of If statement No 2

print("End of Program.")