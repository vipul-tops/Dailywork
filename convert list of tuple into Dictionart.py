# python program to convert list of tuple into Dictionary


lt = [('Vipul',11) , ('Sanjay',12) , ('Rahul',13)]

dic = dict(lt)

print("Dictionary :: ",dic)

# print only keys of dictionay
keys = dic.keys()
print(keys)

values = dic.values()
print(values)


items = dic.items()
print(items)

copy = dic.copy()
print(copy)

# delete an Element from dictionary

marks = {"Vipul":85,"Aksh":65,"Raj":99,"Meera":53}

print(marks)

del marks['Meera']

print(marks)

# delete element using pop function
dicc = {"Any":42,"Raj":63,"Payj":52,"aj":84}

dicc.pop("Payj")

print(dicc)










