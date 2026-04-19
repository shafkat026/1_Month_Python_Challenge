class Student:
    language = "Py"
    SID = 2301026   # class attribute

    def __init__(self, name, language, SID):    # dunder method; called automatically 
        self.name = name
        self.language = language
        self.SID = SID
        print("I am creating an object")




    def getinfo(self):  #must use self; whether use it or not
        print(f"The language is {self.language}. The SID is {self.SID}")
    
    @staticmethod   # if does not use/need "self"
    def greet():
        print("Good Night")

shafkat= Student("Shafkat", "C", 26)
shafkat.language = "CPP"    # instance attribute
print(shafkat.language, shafkat.SID ) 

# abul = Student()