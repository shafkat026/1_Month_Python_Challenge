# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a=26

o=Demo()
print(o.a)  # Prints class attribute as no instance attribute is present

o.a = 0     # instance attribute is set
print(o.a)  # Prints instance attribute as instance attribute is present

print(Demo.a)
