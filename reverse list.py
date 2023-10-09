# reverse list

l = [12,3,9,45,36,95,75]

print("Original List ",l)

x = l[::-1]

print("Reverse list ",x)

l.reverse()

print("reverse list : ",l)

#Reverse a list using the insert()

s = []

for i in l:
    s.insert(0,i)

print(s)
