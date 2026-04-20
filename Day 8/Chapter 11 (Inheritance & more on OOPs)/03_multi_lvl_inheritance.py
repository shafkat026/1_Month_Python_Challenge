class company:
    a = 7

class manager(company):
    b = 6

class employee(manager):
    c=26

o = company()
print(o.a)

# o = company()
# print(o.b)      #shows error

o = manager()
print(o.a, o.b)

o = employee()
print(o.a, o.b, o.c)