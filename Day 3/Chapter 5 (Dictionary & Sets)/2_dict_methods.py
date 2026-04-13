marks={
    "Shafkat":33,
    "Abul": 37,
    "Babul": 73,
    26:"Kabul"
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Shafkat":99, "IDK":50})
print(marks)

print(marks.get("Shafkat")) #if not found, output: None
print(marks["Shafkat"])     #if not found, output: error


marks.pop("Abul")       # removes specific item
print(marks)

marks.popitem()         # removes last item
print(marks)