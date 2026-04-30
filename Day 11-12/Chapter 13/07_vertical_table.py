#  A list contains the multiplication table of 7. 
# write a program to convert it to vertical string of same numbers. 

n = 7

table = [ str(i*n) for i in range(1,11)]
print(table)

v = "\n".join(table)
print(v)
