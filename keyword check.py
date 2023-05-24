import keyword


key=["if", "else","vipul","none","elif","int","Anj","len","str","True","False","list","float"]

for i in range(len(key)):
    if keyword.iskeyword(key[i]):
        print(key[i],"is keyword")
    else:
        print(key[i],"is not keyword")




#print all keyword

print(keyword.kwlist)
