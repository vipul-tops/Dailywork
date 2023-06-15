#python practice

a=15+5j
print(type(a))


#exception handling
a=int(input("Enter A : "))
b=int(input("Enter B : "))

try:
    c=a/b
    print(c)
except:
    print("Exception handle")


#
age=14
msg="You are adult" if age>18 else "You are a Minor"
print(msg)

#
n=(1,2,3,4,5)
sum=0
for num in n:
    sum+=num
print(sum)

#
age={"Alice":25,"Bob":30,"Charlie":35}
for name in age:
    print(age[name])
