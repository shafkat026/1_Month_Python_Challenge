a = int(input("Enter an Int:"))
b = int(input("Enter an Int:")) #if b=0; ZeroDivisionError: division by zero

if(b==0):
    raise ZeroDivisionError("Hey this is not possible")

else:
    print(f"The division a/b is {a/b}")