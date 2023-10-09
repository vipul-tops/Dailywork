# Average of element in list

l3 = [12,64,48,96,25,36]

total = 0
lenth = 0
for k in l3:
    total = total+k
    lenth = lenth+1

print("total :",total)
print("Length : ",lenth)

ave = total/lenth

print("Average :",ave)

for k in l3:
    if k >ave:
        print(k)
