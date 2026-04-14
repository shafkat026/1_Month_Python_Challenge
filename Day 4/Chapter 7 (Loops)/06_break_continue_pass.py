for i in range(100):
    if(i==7):
        continue    # 7 will be skipped
    if(i==26):
        break       # exits the loop at 26
    print(i)





for i in range(100):
    pass            # without pass, the program will throw an error

i=1
while(i<26):  
    print(i)
    i +=1