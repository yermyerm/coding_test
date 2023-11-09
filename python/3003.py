A = [*map(int, input().split())]
B = [1, 1, 2, 2, 2, 8]
ans = []
for a, b in zip(A, B):
    ans.append(str(b-a))
print(' '.join(ans))
