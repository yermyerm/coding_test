N, M = map(int, input().split())
bas = [x for x in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    bas = bas[:i-1] + list(reversed(bas[i-1:j])) + bas[j:]
print(*bas)
