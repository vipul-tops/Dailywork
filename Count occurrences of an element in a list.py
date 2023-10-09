# Count occurrences of an element in a list

l = [10,5,36,10,85,65,15,10]

s = 10

count = 0

for i in l:
    if i==s:
        count +=1

print(l)
print(count)

# using count()

a=l.count(s)

print(a)
