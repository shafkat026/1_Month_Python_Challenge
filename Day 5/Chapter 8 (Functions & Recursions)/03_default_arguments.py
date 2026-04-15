def greetings(name, end= "Merci!"):
    print(f"Good day, {name}")
    print(end)

name = input("Enter your name: ").title()


greetings(name,"Thank You")
greetings(name)