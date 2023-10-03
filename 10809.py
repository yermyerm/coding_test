S = input()
ans = []
for x in list("abcdefghijklmnopqrstuvwxyz"):
    ans.append(str(S.find(x)))

print(' '.join(ans))
