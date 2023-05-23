
#get input from user
b=input("Enter Name: ")
print(b)

#using end arguments
print("vmmemakiya",end="@")
print("gmail.com")

#code for disabling the softspace feature
print("V","M","M",sep="")

#string slicing
s="Hello World"
a=slice(1,10,2)
b=slice(2,6)
print(s[a])
print(s[b])

#string slicing

s="HelloWorld"

print(s[-8:-1])
print(s[:10:3])
print(s[1:10:2])

#string range
for i in range(1,10):
    print(i, end="")

#
print("\n")
a=range(100)
ans=a[:50]
print(ans)


#
s="HELLO"
s1="WORLD"
print("".join([s,s1]))
print("%s %s"%(s,s1))

#set

set1=set("HelloWorld")
print(set1)


set1=set(["Hello","Sete","Ank"])
print(set1)

#add in set
set1=set()

set1.add(8)
set1.add(15)
set1.add((45,6))

print(set1)

set1.update([5,9])
print(set1)


#for loop
set2=set(["Vipul","Ank","web"])
for i in set2:
    print(i)

#remove from set

set2=([1,2,3,4,5,6,7,8,10])

set2.remove(4)
set2.remove(8)
print(set2)

set2=([1,2,3,4,5,6,7,8,10])
set2.pop()
print(set2)












