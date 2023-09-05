N, A = int(input()), [*map(int, input().split())]
A = [a/max(A)*100 for a in A]
print(sum(A)/N)
