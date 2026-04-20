class Employee:
    company = "Example LLC"
    name = "Shafkat"

    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")


class coder:
    language = "Python"

    def printlang(self):
        print(f"Your language is {self.language}")



class Programmer(Employee, coder):
    company = "Example PLC"
    
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printlang()

