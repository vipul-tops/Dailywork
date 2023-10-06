a='apple is best fruit'
print('apple' in a)


ab='hello world'
print(len(ab))

for x in 'banana':
    print(x)

s={12,'sdss',546,'wdwds'}
print(type(s))

# pattern

n=9

for i in range(1,n):
    for j in range(-1+i,-1,-1):
        print(format(2**j,"3d"),end=' ')
    print("")

print("-"*40)
# fibonacci

n=int(input("Enter N : "))

a,b=0,1
print(a,end=" ")

while b<n:
    print(b,end=" ")
    a,b=b,a+b

print("-"*40)
# factorial
n=int(input("Enter N : "))

fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact)

print("-"*40)
# prime number
num=int(input("Enetr num : "))

if num == 2:
    print(num,"is Prime Number")
    
elif num <=1 or num % 2 == 0:
    print(num,"is not prime")

else:
    for i in range(3, int(num ** 0.5) + 1,2):
        if num % i == 0:
            print(num,"is not prime")
            break
    else:
        print(num,"is prime")

print("-"*40)
# square pattern

n=5

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==1-n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

print("-"*40)
# sort without using sort

li=[12,8,96,34,787,3,34,48,45,32,65]

n= len(li)

for i in range(n):
    for j in range(i+1,n):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]

print(li)

# sort list
li=[12,8,96,34,787,3,34,48,45,32,65]

n=sorted(li, reverse=True)

print(n)

print("-"*40)
# palindrome

s="nitin"
if s==s[::-1]:
    print("yes ")
else:
    print("No")

print("-"*40)
# sort dictionary

di={45:'vipul',23:'husd',96:'sgs',36:'dsdsd'}

d=sorted(di.keys())

di2={}

for i in d:
    di2[i]=di[i]

print(di2)


print("-"*40)
# find the output

s='the sky blue'
l=s.split()
l=l[::-1]
l=' '.join(l)
print(l)


print("-"*40)
# find the output

l=[4,56,38,63,84,45,91,12]

maxi=l[0]
minm=l[0]

for i in l:
    if i>maxi:
        maxi=i
    if i<minm:
        minm=i

print("max : ",maxi)
print("min : ",minm)





















