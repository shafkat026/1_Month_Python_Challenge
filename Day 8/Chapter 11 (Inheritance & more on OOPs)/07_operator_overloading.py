class num:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
        
        
n = num(1)
m = num(2)

print(n + m)