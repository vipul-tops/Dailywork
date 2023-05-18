
#use of (+) operator
t1=(12,19,94,91,91,75)
t2=("Tuple","Index")

t3=(t1+t2)
print(t3)

print(t1+t2)

# nested tuple
t4=(t1,t2)
print(t4)

#repetitation tuple

tpl=("Project","Wallet")*3
print(tpl)

tpl=("python")*5
print(tpl)

#slicing

t=(1,2,3,4,7,96,35,46,93,12)

print("\n",t)

print(t[:5])
print(t[2:9])
print(t[1:9:2])

print(t[::-1])

print(t[-10:-1])

print(t[-10:-1:2])

#without using bracket()
tpl=1,2,3,4,"JAVA",True
print(tpl)



