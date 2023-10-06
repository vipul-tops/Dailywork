#string
#fibonacii serires
#swap
#pattern

n=int(input("Enter N : "))
a,b=0,1
print(a,end=" ")

while b<n:
    print(b,end=" ")
    a,b=b,a+b

print()

n=5
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()

for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()

stri="DsdfIIJKNKDS"
print(stri.lower())

print(len(stri))
ch=0
for i in stri:
    ch+=1
print(ch)



num=int(input("Enter N : "))

fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact)

#prime Number 
nu=int(input("Enter N : "))

if nu==2:
    print("Prime Number")
elif nu<=1 or nu%2==0:
    print("Not Prime Number")
else:
    for i in range(3,int(nu**0.5)+1,2):
        if nu%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")

builtin_names = dir(__builtins__)
for name in builtin_names:
    print(name)










