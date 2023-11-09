words = open(0).read().split()[1::]
ans = 0
for word in words:
    chars_unique = []
    chars = []
    for i in range(len(word)):
        if (i == 0 or word[i] != word[i-1]):
            chars += word[i]
            if word[i] not in chars_unique:
                chars_unique += word[i]
    if chars_unique == chars:
        ans += 1
print(ans)
