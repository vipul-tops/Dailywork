
#tuple

t=("Python","Java","Web")
print(t)


value:tuple [int | str,...]=(1,2,3,"Vipul")
print(value)


mytuple=("Vipul",)  #separated by comma(,)
print(type(mytuple))

#not tuple
tpl=("Vipul")
print(type(tpl))

#tuple constructor

tpl_cons=tuple(("Python","Java",1,2,3,"WEB"))
print(tpl_cons)


t=("Hello","World","Ankit","Pt")
print("\n",t)
print(t[2])
print(t[3])

#negative index

t=("Python","Tuple","List",True)

print("\n",t)
print(t[-1])
print(t[-4])

#tuple index
t=("Web","Python","Vs",45,96,37,"Sec")
a=t.index("Python")
print(a)


#
t=("Python","Samay",15,63,"pycharm")
b=t.count(15)
print(b)

#sort
t=(5,63,42,78,94,45)
b=sorted(t,reverse=True)
print(b)

#
t=(5,63,42,78,94,45)
b=sorted(t)
print(b)

#
t=("Hello","World","Ankit","Pt")
b=sorted(t)
print(b)

#
t=("Hello","World","Ankit","Pt")
b=sorted(t,reverse=True)
print(b)

#
t=("Hello","World","Ankit","Pt","A")
b=sorted(t,reverse=True,key=len)
print(b)

#

def sec(el):
    return el[0]

t=((2,23),(9,45),(4,11),(3,51))
b=sorted(t,reverse=False,key=sec)
print(b)

#
def acc(el):
    return el[1]

t=((2,23),(9,45),(4,11),(3,51))
b=sorted(t,reverse=False,key=acc)
print(b)

#minimum element

tpll=(84,63,12,67,45,35)
a=min(tpll)
print(a)

tup=((15,35),(78,15),(13,56),(13,78))
a=min(tup)
print(a)


#max tuple

tpll=(84,63,12,67,45,35)
a=max(tpll)
print(a)


tup=((15,35),(78,15),(13,56),(13,15))
a=max(tup)
print(a)
b=max(tup[2])
print(b)






