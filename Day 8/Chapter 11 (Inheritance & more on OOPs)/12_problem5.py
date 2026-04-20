#  Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them. 


# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, x , y , z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v2):

        Vadd = Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)
        return Vadd
    
    def __mul__(self, v2):
        
        result = self.x * v2.x + self.y * v2.y + self.z * v2.z
        return result
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __len__(self):
        return 3
    
v1 = Vector(1,2,3)
v2 = Vector(7,8,9)
v3 = Vector(3,2,1)

print(f"Length of v1 is {len(v1)}")

print(v1 + v2)
print(v1 * v2)

print(v2 + v3)
print(v2 * v3)

print(v1 + v3)
print(v1 * v3)

        