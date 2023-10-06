# Count Positive and Negative number from list

l = [1,3,-4,78,-9,30,15,-10]

c_positive = 0
c_negative = 0

for i in l:
    if i<0 :
        c_negative +=1

    elif i>0:
        c_positive +=1

print(c_positive)
print(c_negative)
