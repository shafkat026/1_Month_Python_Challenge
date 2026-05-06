# Unit Converter (Civil Edition)

# m ↔ ft
# m² ↔ ft²
# m³ ↔ CFT


while True:
    print("1. m → ft\n2. ft → m\n3. m³ → CFT\n4. CFT → m³ \n0. Exit\n")
    choice = input("Choose: ")

    if choice == "1":
        m = float(input("Meters: "))
        print("Feet:", m * 3.28084)

    elif choice == "2":
        ft = float(input("Feet: "))
        print("Meters:", ft / 3.28084)

    elif choice == "3":
        m3 = float(input("m³: "))
        print("CFT:", m3 * 35.3147)

    elif choice == "4":
        CFT = float(input("m³: "))
        print("m³:", CFT * 35.3147)

    elif choice == "0":
        break
    else:
        print("Invalid choice")