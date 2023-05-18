#tuple length

t=(15,3,48,"Web",False,6)

print(len(t))

#find index 
a=t.index(False)
print(a)

t=(15,3,48,"Web",False,6,45,63)
if "Web" in t:
    print("Yes, Web available in this tuple")

#convert tuple into list

t=(15,3,48,"Web",False,6)

l=list(t)
print(l)

l.append("Java")

print(l)

t=tuple(l)

print(t)

#add tuple to tuple
t=("ABC",45,96,"POI",12.2)
q=("Web",45)

t+=q
print(t)


#convert tuple to list and remove items
t=(15,3,48,"Web",False,6)
l=list(t)
l.remove(False)
t=tuple(l)
print(t)

#unpack tuple

tpl=("ABC","QWE","ZXC")
(ABC,QWE,ZXC)=tpl
print(ABC)
print(ZXC)


#use of astrik *
tpl=("JAVA","ankiy","red","colour","pillow")
(JAVA,ankiy,*red)=tpl
print(JAVA)
print(red)

#use of * tropic
tpl=("JAVA","ankiy","red","colour","pillow")
(abc,*tropic,acc)=tpl
print(abc)
print(tropic)
print(acc)

#nested tuple

t=("Sanjay","Kaushik",["Sahil","Vivek"],15)
print(t[2])

print(t[2][1])

t[2][1]="Jay"
print(t)










