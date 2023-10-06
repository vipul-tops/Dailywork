# remove empty tuple from list

l = [12,(),8,98,(),65,32,(),(15,4),6]

t = list(filter(None,l))

print(t)
