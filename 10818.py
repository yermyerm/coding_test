N = input()
A = list(map(int, input().split()))
print(max(A), A.index(max(A))+1)
