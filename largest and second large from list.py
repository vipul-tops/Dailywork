# largest/Smallest number from list

l = [23,43,65,45,67,72,87,48]

largest = 0
small = 0

second_largest = 0

for i in l:
    if i >= largest:
        largest = i
print(largest)

for i in l:
    if i < largest and i > small and i :
        small = i
        second_largest = i
print(second_largest)
