n=int(input("Enter N : "))

a,b=0,1
print(a,end = " ")
for i in range(n-1):
    print(b,end=" ")
    a,b=b,a+b
print()

num=int(input("Enter N : "))

if num==2:
    print(" Prime")

elif num<=1 or num%2==0:
    print("Not Prime")

else:
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
# factorial
nn=int(input("Enter N : "))

fact=1

for i in range(1,nn+1):
    fact=fact*i
print(fact)


print()

#remove duplicate element

l=[1,24,6,8,9,1,3,4,8]

l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
print(l1)


#counting

s =input("Enter String : ")

w=1
ch=0
sp=0
spc=0
d=0

for i in s:
    if i.isalpha():
        ch = ch+1
    elif i.isnumeric():
        d= d+1
    elif i.isspace():
        w=w+1
        spc=spc+1
        sp=sp+1

print("ch :",ch)
print("d :",d)
print("w : ",w)
print("spc : ",spc)

# dictionary

d={}

a=int(input("Enter A :"))

for i in range(1,n):
    d[i]=i*i
print(d)











