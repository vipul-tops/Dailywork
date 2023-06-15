# student result

rno=int(input("Enter Roll No. : "))
sname=input("Enter Student Name : ")

s1=int(input("Maths : "))
s2=int(input("English : "))
s3=int(input("Account : "))
s4=int(input("Business : "))
s5=int(input("Economics : "))

total=s1+s2+s3+s4+s5
per=total/5

print("Roll No. : ",rno)
print("Student Name : ",sname)
print("Total : ",total)
print("Percentage : ",per)

if per>=70:
    print("Distiction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass")
else:
    print("Fail")

