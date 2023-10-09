# difference element

l1 = [12,34,8,96,"tops"]
l2 = [34,96,"tops",36,10,77]

l3 = []

for i in l1:
    for j in l2:
        if i not in l2 and i not in l3:
            l3.append(i)

        elif j not in l1 and j not in l3:
            l3.append(j)
        else:
            pass

print("list 1 ",l1)
print("list 2 ",l2)
print("Unique Element: ",l3)


