import copy

# copy list

l1 = [15,30,84,35,"anjj",61]

l2 = l1[:]

print(l2)


#

l3 = copy.copy(l2)

print(l3)

#
l4 = [i for i in l3]

print(l4)


#
ll = [45,36,84,3]

l5 = map(int,ll)

print(*l5)
