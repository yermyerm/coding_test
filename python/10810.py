N, M = map(int, input().split())
bas = []
for i in range(N):
    bas.append("0")
for i in range(1, M+1):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        bas[x] = str(k)
print(' '.join(bas))
