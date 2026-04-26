try:
    a = int(input("Enter Int:"))
    print(a)
  
except Exception as e:
    print(e)

else:
    print("else") 
    #if try block is true, then it will go to else
    # This is executed only if the try was successful 