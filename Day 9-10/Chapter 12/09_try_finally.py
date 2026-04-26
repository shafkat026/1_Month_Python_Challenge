def main():

    try:
        a = int(input("Enter Int:"))
        print(a)
        return a
    
    except Exception as e:
        print(e)

    finally:
        print("finally") # This will be executed no matter what happens with try block 

    print("out of finally") # This will be executed only if the try block is unsuccessful 

main()
        