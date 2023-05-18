
#list Comprehensive
square=[x **2 for x in range(1,11) if  x%2==1]
print(square)


print("\n")
#2

square=[]
for x in range(1,11):
    square.append(x**2)

print(square)

#3
print("\n")

fruit=["Apple","Banana","Orange","Mango","Pineple"]
nl=[]

for x in fruit:
    if "a" in x:
        nl.append(x)
print(nl)


print("\n")
#4
l=[character for character in [1,2,3]]

print(l)

#5
print("\n")
l=[x for x in range(11) if x%3==0]
print(l)

#6
l=[]

for char in "Vipul Memakiya":
    l.append(char)

print(l)
    
