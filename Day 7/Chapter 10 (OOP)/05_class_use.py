class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, ID):
        self.name= name
        self.salary = salary
        self.ID = ID

p = programmer("Shafkat", 5000, "MS126")
print(p.name, p.salary, p.ID, p.company)

p = programmer("Abul", 4000, "MS127")
print(p.name, p.salary, p.ID, p.company)