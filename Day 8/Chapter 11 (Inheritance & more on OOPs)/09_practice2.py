#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animals:
    def __init__(self):
        print("This is Animals class")

class Pets(Animals):
    def __init__(self):
        super().__init__()   # call Animals constructor
        print("This is Pets class")

class Dog(Pets):
    def __init__(self):
        super().__init__()   # call Pets constructor
        print("This is Dog class")
    
    
    def bark(self):
        print("Dog is barking")


# Creating object
d = Dog()
d.bark()
