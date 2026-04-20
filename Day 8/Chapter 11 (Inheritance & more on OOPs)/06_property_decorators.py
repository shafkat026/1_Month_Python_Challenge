class student:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

s = student()
s.a =26
s.name = "Shafkat Sadik"

print(s.name)
print(s.fname, s.lname)
print(s.fname)
print(s.lname)

s.show()