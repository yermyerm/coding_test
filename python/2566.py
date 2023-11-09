N = [list(map(int, input().split())) for _ in range(9)]
ans = 0
coordi = [1, 1]
for i, n in enumerate(N):
    if max(n) > ans:
        ans = max(n)
        coordi = [i+1, n.index(ans)+1]
print(ans, ' '.join(list(map(str, coordi))), sep='\n')
