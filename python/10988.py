word = input()
ans = 1
for i in range(len(word)//2+1):
    if word[i] != word[-1-i]:
        ans = 0
        break
    else:
        continue
print(ans)
