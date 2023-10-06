# generator in Python

def my_fun():

    yield 1

x = my_fun()

print(x)   # generator return object

#print(x.__next__())  # return value

print(next(x))



# print even number

def myfun(n):
    a=0
    
    while a<n:
        
        if a%2==0:
            yield a
        a +=1

y = myfun(20)

for i in y:
    print(i,end = " ")


print("-"*40)

# fibanacii series

def fibo(n):

    a,b=0,1

    while b<n:

        yield a

        a,b = b,b+a

z = fibo(10)

for i in z:
    print(i)















