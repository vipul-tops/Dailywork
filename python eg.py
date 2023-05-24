#addition
a=int(input("Enter A : "))
b=int(input("Enter B : "))

print(a+b)

for i in range(1,10):
    print("*" * (9-i),* " ")

for i in range(1,10):
    print(" " *(9-i),"*"*i)

for i in range(1,10):
    print(i * (9-i))

#if else

a=int(input("Enter A : "))
if a>0:
    print("It is Positive Number")
else:
    print("It is negative Number")

#odd even number

a=int(input("Enter A : "))
if a%2==0:
    print("Even Number")
else:
    print("Odd Number")

#greater Number

a=int(input("Enter A : "))
b=int(input("Enter B : "))
if a>b:
    print("A is Greater ")
else:
    print("B is Greate rnumber")


#nested if else greater number
a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if b>c:
        print("A is Greater")
    else:
        print("A is Greater ")
elif b>c:
    print("B is Greater")
else:
    print("C is Greater")



















