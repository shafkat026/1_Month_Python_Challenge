class company:
    def __init__(self):
        print("Constructor of company")
    a = 7

class manager(company):
    def __init__(self):
        print("Constructor of manager")
    b = 6

class employee(manager):
    def __init__(self):
        super().__init__()
        print("Constructor of employee")
    c=26

o = company()
print(o.a)


o = manager()
print(o.a, o.b)

o = employee()
print(o.a, o.b, o.c)