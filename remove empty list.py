# remove empty list from list

li=[12,65,37,[],45,98,[],2]

l1 = list(filter(None,li))

print(l1)


#
l = [15,[],3,97,[],6]

l2 = []

for i in l:
    if i:
        l2.append(i)
print(l2)
