with open("Hi-score.txt") as f:
    text =f.read()

with open("file_copy.txt", "w") as g:

    g.write(text)

