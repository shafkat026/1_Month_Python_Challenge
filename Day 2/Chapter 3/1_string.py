name ='Shafkat'       # Single quoted string 
b = "Shafkat"      # Double quoted string 
c = '''Shafkat'''  # Triple quoted string 

length= len(name)
print(length)

#sl = name [ind_start:ind_end]
nameshort = name[0:3]   #start from index 0 all the way till 3 (excluding 3)
print(nameshort)
nameshort = name[1:3]   #start from index 1 all the way till 3 (excluding 3)
print(nameshort)

char1= name[1]
print(char1)


#Negative Slicing

name2= "SHAFKAT"

print(name2[-4:-2])
print(name2[3:5])   #both are same

print(name2[:5])    # 0-5
print(name2[3:])    # 3-(n-1)
