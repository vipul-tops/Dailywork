
#Using of .append()
l=[]
print("Blank List : ")

print(l)
l.append(12)
print(l)
l.append(15)
l.append(45)
l.append("Python")
print(l)

for i in range(10,30,5):
    l.append(i)

print(l)

list=["Hello","World"]

l.append(list)

print(l)

#using of .insert()
print("\n")
l=[1,2,3,4,5,6]
print(l)

l.insert(3,10)
print(l)
l.insert(3,"List")
print(l)

#using of .extend() method

print("\n")
l=[12,78,63,92]
print(l)
l.extend(["Hello",12,"Java"])
print(l)

