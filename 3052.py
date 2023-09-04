list = [*map(int, open(0).read().split())]
ans = []
for i in list:
    if i % 42 not in ans:
        ans.append(i % 42)
    else:
        continue
print(len(ans))
