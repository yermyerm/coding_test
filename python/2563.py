N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
dup = 0
for i in range(len(S)):
    for s in S:
        if s != S[i]:
            if abs(S[i][0]-s[0]) < 10 and abs(S[i][1]-s[1]) < 10:
                dup += (10-abs(S[i][0]-s[0]))*(10-abs(S[i][1]-s[1]))
print(100*N-round(dup*1/2))
