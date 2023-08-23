n=9

for i in range(1,n):
    for j in range(-1 + i,-1,-1):
        print(format(2 ** j,"3d"),end=' ')
    print("")


print("-"*40)

n=int(input("Enter N :"))

a,b=0,1
print(a,end=" ")

while b<n:
    print(b,end=" ")
    a,b=b,a+b
