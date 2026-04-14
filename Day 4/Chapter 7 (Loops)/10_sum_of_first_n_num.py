# Write a program to find the sum of first n natural numbers using while loop. 

n=int(input("Enter Number:"))

i=1
sum=0
while(i<=n):
    sum=sum+i
    # print(i)    #done for checking increment
    i+=1
print(sum)