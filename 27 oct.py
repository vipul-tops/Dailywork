# factorial
'''
n = int(input("Enter N : "))

fact = 1

for i in range(1,n+1):
    fact = fact*i

print("Factorial : ",fact)
print()

# count character from string


s = "This is the Example"

count = 0
ch=0

for j in s:
    if "i" in j:
        count +=1

print("Count I : ",count)

for k in s:
    ch+=1
print(ch)


# compare two string

st = "Hello World"

st1 = "Hello World"

if st == st1:
    print("True")

else:
    print("False")


def comp():

    l1 = ["hello"]

    l2 = ["hello"]

    if l1 ==l2:
        print("True")

    else:
        print("False")

comp()


# sum of element

l = [1,2,6,8,9]

total = 0

for i in l:
    total = total + i
print(total)
print("*"*30)

# sum of user element 
li = []
tot = 0
def fun(li,tot):
    n = int(input("Enter N : "))

    for j in range(1,n+1):
        el = int(input("Enter Element : "))
        li.append(el)

    print(li)

    for ij in li:
        tot = tot + ij

    print(tot)

fun(li,tot)
'''

# sort ascending

ab = [12,6,37.98,25]
print(ab)
def abc(ab):
    s = sorted(ab,reverse=True)

    print(s)

abc(ab)

