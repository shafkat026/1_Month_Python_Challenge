from functools import reduce

l = [1,2,3,4,5]

# Map

sq= lambda x : x*x

sqList = map(sq, l)
print(list(sqList))


# Filter

def even(n):
    if(n%2 ==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))


# Reduce

def sum(a,b):
    return a+b
# def multi(a,b):
#     return a*b
multi = lambda x,y: x* y

print(reduce(sum,l))
print(reduce(multi,l))