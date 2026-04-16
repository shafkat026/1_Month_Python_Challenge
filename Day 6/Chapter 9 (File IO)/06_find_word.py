word=input("Enter word to search:\t")


# f = open("poem.txt")
# a=f.read()
# a=a.lower()


# if (word in a):
#     print(f"\"{word.title()}\" is present in the poem")
# else:
#     print(f"\"{word.title()}\" is not present in the poem")

# f.close()





with open("poem.txt", "r") as f:
    
    lines=f.readlines()

lineno= 1
for line in lines:
    if (word in line):
        print(f"\"{word.title()}\" is present in the poem Line no: {lineno}")
        break
    lineno +=1

else:
    print(f"\"{word.title()}\" is not present in the poem")
        