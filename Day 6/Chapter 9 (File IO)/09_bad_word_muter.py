words = ["Donkey", "idiot"]

with open("bad.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"* len(word))

with open("bad.txt", "w") as f:
    f.write(content)