N = open(0).read().split()
ans = ""
for i in range(max(map(len, N))):
    for n in N:
        if len(n) > i:
            ans += n[i]
print(ans)
