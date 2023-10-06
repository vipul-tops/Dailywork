# remove even element from list

l = [15,88,62,11,66,91,50]

for i in l:
    if i%2==0:
        l.remove(i)

print(l)


# remove element using slicing 

l1 = [12,45,36,95,62,44,10]

del l1[1:5]

print(l1)
