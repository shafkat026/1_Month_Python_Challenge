class calculator():
    def __init__(self, n):
        self.n = n

    def sq(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def sqrt(self):
        print(f"The square root is {self.n **1/2}")

    @staticmethod
    def hello():
        print("Hello There!")
        

num=int(input("Enter a number:"))

a = calculator(num)
a.sq()
a.cube()
a.sqrt()
a.hello()