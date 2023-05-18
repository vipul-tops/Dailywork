
#for loop in tuple

tpl=("JAVA","ankiy","red")
for x in tpl:
    print(x)

# loop through index number
tpl=("JAVA","ankiy","red","colour")

for x in range(len(tpl)):
    print(x)

#while loop

tpl=("JAVA","ankiy","red","colour","pillow")
x=0
while x <len(tpl):
    print(tpl[x])
    x=x+1
    
#
tpll=("**")
n=5
for i in range(int(n)):
    tpll=(tpll,)
    print(tpll)
