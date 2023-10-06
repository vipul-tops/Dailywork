# Print Duplicate from List of Integer

l = [12,45,6,97,12,3,6,52,31,12]

uni_list = []
dup_list = []

for i in l:
    if i not in uni_list:
        uni_list.append(i)

    elif i not in dup_list:
        dup_list.append(i)

print("Original List : ",l)

print("Unique List ",uni_list)
print("Duplicate List ",dup_list)
