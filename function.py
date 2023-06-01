#function

def getdata():
    print("Hello World")

getdata()

#
def calculator(a,b):
    print("Addition : ",a+b)
    print("Substraction : ",a-b)
    print("Multiplication : ",a*b)
    print("Division : ",a/b)

calculator(10,5)
calculator(45,9)
calculator(82,2)


#keyword arguments
def great(fname,lname):
    print("Hello !!",fname,lname)

great("Ankit",lname="Kumar")


#default arguments
def fun(name="Guest"):
    print("Hello !!",name)

fun("Vijay")


#variable argument

def test(*args):
    print(args)
    print(type(args))
    print(len(args))

test("India","Python","Ant")






















