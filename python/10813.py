N, M = map(int, input().split())
bas, ans = [], []
for i in range(N):
    bas.append(str(i+1))
for x in range(M):
    i, j = map(int, input().split())
    bas[i-1], bas[j-1] = bas[j-1], bas[i-1]
print(' '.join(bas))
