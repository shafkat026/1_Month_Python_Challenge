s= {34,1,2,3,33,3,4,"Shafkat"} 

s.add(67)
s.remove(1)
print(s)


s1={5,6,7}
s2={2,7,8,9}

print(s.union(s1))
print(s2.intersection(s1))
print(s1-s2)
print(s2-s1)

print({2,7}.issubset(s2))