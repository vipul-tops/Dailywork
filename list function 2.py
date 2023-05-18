#count

l=["Ankit",10,45,"Ankit",96,71,True,"Python"]

print(l)

print(l.count("Ankit"))
#index
print(l.index(71))
print(l.index("Ankit",1))

#pop
l.pop(5)
print(l)

#extend
list=["Hello","Developer"]
l.extend(list)
print(l)

#copy
list1=l.copy()
print(list1)

list1=l[:]
print(list1)

#sort

l=[10,34,69,15,7,100]

l.sort()
print(l)

l.sort(reverse=True)  #descending order
print(l)

#reverse

l=["Ankit",10,45,"Ankit",96,71,True,"Python"]
l.reverse()
print(l)

#remove
l.remove(10)
print(l)

l=[1,2,3,4,5,6,9,12,45,63,78]
for i in range(1,6):
    l.remove(i)
print(l)



