# Write a program to print multiplication table of a given number using for loop. 
n=int(input("Table for:\t"))

for i in range(1,11):
    print(n, "x", i, "=", n*i)

i=1
while(i<=10):
    print(n, "x", i, "=", n*i)
    i+=1
