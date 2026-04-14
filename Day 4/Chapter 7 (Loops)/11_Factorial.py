# using for loop. 

num=int(input("Enter Number:"))

n=1

# for i in range(2,num+1):
#     n=n*i
# print("Factorial of", num, "is", n)


i=1
while(i<=num):
    n=n*i
    i+=1
print(f"Factorial of {num} is {n}")