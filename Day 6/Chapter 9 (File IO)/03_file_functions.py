f =open("poem.txt")

# lines=f.readlines()
# print(lines, type(lines))




# line1=f.readline()
# print(line1, type(line1))

# line2=f.readline()
# print(line2, type(line2))

# line3=f.readline()
# print(line3, type(line3))

# line4=f.readline()
# print(line4, type(line4))

# line5=f.readline()
# print(line5, type(line5))

# line6=f.readline()
# print(line6, type(line6))

# line7=f.readline()
# print(line7, type(line7))

# line8=f.readline()
# print(line8, type(line8))

# line9=f.readline()
# print(line9=="")        #cant jump to 10. it will show line 9 first 



line=(f.readline())
while(line !=""):
    print(line)
    # line = f.readline()

f.close()