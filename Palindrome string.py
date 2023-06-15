
#String is a Palindrome

myStr = input("Enter Any String : ")
j = myStr
rev = ""

while len(j) > 0:
    if len(j) > 0:
        a = j[-1]
    j = j[:-1]
    rev = rev + a
    
print("The reverse of string is:", rev)

if rev == myStr:
    print("The given string is Palindrome.")
else:
    print("The given string is not Palindrome.")

