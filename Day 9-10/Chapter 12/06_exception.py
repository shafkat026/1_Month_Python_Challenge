try:
    a = int(input("Enter Int:"))
    print(a)
except ValueError as v:
    print(v)
    print("Heyyy!")
except Exception as e:
    print(e)

print("Thanks")