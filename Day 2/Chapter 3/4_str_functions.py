str = 'Shafkat' 
name = "sadik is"

print(len(str))
print(str.endswith("kat"))
print(str.endswith("Kat"))      #case sensitive; false
print(str.startswith("Sha"))

print(name.capitalize())    #1st letter of 1st words
print(name.title())         #1st letter of all words
print(str.lower())  # shafkat
print(str.upper())  # SHAFKAT


text = "  hello  "
print(text.strip())  # "hello"; Removes spaces from start & end

text = "hello world"
print(text.find("world"))  # 6

text = "banana"
print(text.count("a"))  # 3


GoT="You know nothing, John Snow"
print(GoT.replace("nothing", "something"))

text = "a,b,c"
print(text.split(","))  # ['a', 'b', 'c']

lst = ['a', 'b', 'c']
print("-".join(lst))  # a-b-c

print("abc".isalpha())   # True
print("123".isdigit())   # True
print("abc123".isalnum()) # True


#f-strings
name = "Shafkat"
age = 21
print(f"My name is {name} and I am {age}")





#.split(), .join(), .replace() → super useful in data cleaning
#.isdigit() → useful when parsing numeric data from files
#f-strings → best for clean output in reports & logs