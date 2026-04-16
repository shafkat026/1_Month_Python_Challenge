f =open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement:

with open("file.txt") as f:
    f.read()
    print(f.read())

#no need to close the file now