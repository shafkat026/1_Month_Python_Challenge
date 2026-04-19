class Student:
    language = "Py"
    SID = 2301026   # class attribute

    def getinfo(self):  #must use self; whether use it or not
        print(f"The language is {self.language}. The SID is {self.SID}")
    
    @staticmethod   # if does not use/need "self"
    def greet():
        print("Good Night")

shafkat= Student()
shafkat.language = "CPP"    # instance attribute
print(shafkat.language, shafkat.SID ) 

shafkat.greet()

shafkat.getinfo()
Student.getinfo(shafkat)    #same