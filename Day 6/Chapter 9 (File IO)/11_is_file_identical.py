with open("file.txt") as f:
    text1 =f.read()

with open("file_copy.txt") as f:
    text2 =f.read()

if (text1 == text2):
    print("identical")
else:
    print("not identical")

