#using reverse()

l=[12,45,"Data",785,"Web"]
print(l)
l.reverse()
print(l)

#using remove method
print("\n")

l=[78,12,52,48,"Arav","Tops",45]
print(l)
l.remove(52)
print(l)

print("\n")

#remove using for loop
l=[1,2,4,5,6,78,96,3,8]
print(l)

for i in range(1,4):
    l.remove(i)

print(l)

#using .pop method
print("\n")

l=[15,96,36,25,78]
print(l)

l.pop()
print(l)

print("Remove Specific elements")
l.pop(2)
print(l)

print("\n")



