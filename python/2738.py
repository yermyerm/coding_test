N, M = map(int, input().split())
A = [list(map(int, input().split())) for n in range(N)]
B = [list(map(int, input().split())) for n in range(N)]
answer = []
for a, b in zip(A, B):
    ans = []
    for c, d in zip(a, b):
        ans.append(str(c+d))
    answer.append(' '.join(ans))
print('\n'.join(answer))
