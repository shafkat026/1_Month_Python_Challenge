def g():
    a=int(input("Enter 1st Integer:"))
    b=int(input("Enter 2nd Integer:"))
    c=int(input("Enter 3rd Integer:"))

    if(a>b and a>c):
        print(f"{a} is the greatest of all.")
    elif(b>a and b>c):
        print(f"{b} is the greatest of all.")
    else:
        print(f"{c} is the greatest of all.")


g()




# def find_greatest(a, b, c):

#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c


# a = int(input("Enter 1st Intege: "))
# b = int(input("Enter 2nd Integer: "))
# c = int(input("Enter 3rd Integer: "))

# greatest = find_greatest(a, b, c)

# print(f"{greatest} is the greatest of all.")