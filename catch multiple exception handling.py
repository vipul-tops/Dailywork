
#catch multiple exception handling using python

s=input("Enter String : ")

try:
    n=int(input("Enter Number : "))

    print(s + n)
except (TypeError,ValueError) as a:
    print(a)

print("Exception Handling...")