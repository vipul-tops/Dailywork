
#list comprehensive

Is= [i for i in range(1,10)if i%2==0]
print(Is)

#dict comprehensive

d1={n:n*n for n in range(1,10)}
print(d1)

#
s=5
for i in range(0,s):
    for j in range(0,s):
        if i==0 or i==s-1 or j==0 or j==s-1:
            print("*",end="")
        else:
            print("$",end="")
    print()
