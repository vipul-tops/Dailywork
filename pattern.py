for i in range(5):
    print("*"*i)

"""
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1"""



rows = 9
for i in range(1, rows):
    for j in range(-1 + i, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    print("")


r=5
for i in range(r+1):
    for j in range(i):
        print(i,end=" ")
        
    print("")



        
