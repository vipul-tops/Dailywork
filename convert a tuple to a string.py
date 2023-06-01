#Write a Python program to convert a tuple to a string. 


t=("Py","t","h","o","N")
s=" "
for i in t:
    s=s+i

print("Tuple :",t)
print("String :",s)

print("-------------------------------")

#
t=("P","y","t","ho","N")
s=" "
s=s.join(t)

print("Tuple :",t)
print("String :",s)
