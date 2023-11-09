T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    ans = ""
    for x in list(S):
        ans += x*R
    print(ans)
