
# open("filename", "mode of opening(read mode by default)") 
f = open("file.txt", "r")   #f = open("file.txt")   

data = f.read()

print(data)

f.close()   # must close opeded files, good practice