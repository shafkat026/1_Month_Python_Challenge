# Write a program to open three files a.txt, b.txt and c.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same. 

try:
    with open("a.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("b.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("c.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)
    
print("Hudai !")