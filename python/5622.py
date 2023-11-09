num = input()
ans = []
for x in num:
    for a, b in enumerate(['', 'ABC', 'DEF',
                           'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'], start=1):
        if b.find(x) is not -1:
            ans.append(str(a+1))
print(sum(map(int, ans)))
