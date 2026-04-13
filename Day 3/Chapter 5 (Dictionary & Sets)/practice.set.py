# 1. Write a program to create a dictionary of words with values as their English translation. 
# Provide user with an option to look it up! 

words={
    "I":"je",
    "You": "tu"
}

word = input("ENter the word you want meaning of:")

print(words[word])


# 2. Write a program to input 5 numbers from the user and display all the unique numbers (once).

s=set()

n=input("Enter Number 1:")
s.add(int(n))
n=input("Enter Number 2:")
s.add(int(n))
n=input("Enter Number 3:")
s.add(int(n))
n=input("Enter Number 4:")
s.add(int(n))
n=input("Enter Number 5:")
s.add(int(n))

print(s)



# 3. Create an empty dictionary. Allow 3 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

# 4. Assume that 2 of them have same names. 

d={}

a=input("Enter Your Name:")
b=input("Enter Language Name:")
a=input("Enter Your Name:")
b=input("Enter Language Name:")
a=input("Enter Your Name:")
b=input("Enter Language Name:")

d.update({a:b})

print(d)


