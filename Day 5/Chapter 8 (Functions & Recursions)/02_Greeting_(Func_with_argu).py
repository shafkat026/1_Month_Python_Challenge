def greetings(name, end):
    print(f"Good day, {name}")
    print(end)

    return 26 #not necessary

name = input("Enter your name: ").title()

greetings(name,"Thank You")
greetings("Shafkat", "Merci!")  # Merci = Thanks

a= greetings(name,"Thank You")
print(a)