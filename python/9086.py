case = open(0).read().split()
for i in case:
    if i.isupper():
        print(i[0]+i[-1])
