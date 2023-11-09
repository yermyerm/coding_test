import sys
A = list(map(int, sys.stdin.read().split()))
print(f"{max(A)}\n{A.index(max(A))+1}")
