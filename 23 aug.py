# ** Remove duplicate element from list **

# using build in function
li=[15,6,98,35,45,15,3,17,6]
uni_list=list(set(li))  
print(uni_list)

print("-"*40)

# Without using build in function

li=[15,6,98,35,45,15,3,17,98]

l=[]

for i in li:
    if i not in l:
        l.append(i)
print(l)

print("-"*40)

# using list comprehensive

li=[16,11,48,62,9,21,17,11,3,98]
l=[]

[l.append(i) for i in li if i not in l]
print(l)

print("-"*40)

# Print only Duplicate elements of list

li=[15,6,98,17,35,45,15,3,17,98]

l=[]

seen=set()

for i in li:
    if i in seen:
        l.append(i)
    else:
        seen.add(i)
print(l)

print("-"*40)

#print only smallest elements from list

li=[16,11,48,62,9,21,17,11,3,98]

l=li[0]

for i in li:
    if i < l:
        l=i
print(l)


print("-"*40)

#print only largest elements from list

li=[16,11,48,62,9,21,17,11,3,98]

l=li[0]

for i in li:
    if i>l:
        l=i

print(l)











