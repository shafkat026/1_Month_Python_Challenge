# Write a program to filter a list of numbers which are divisible by 5. 

myList = [1,4,5,8,10,11,16,20,25]

def five(n):
    if(n%5 ==0):
        return True
    return False

onlyFive = filter(five, myList)
print(list(onlyFive))