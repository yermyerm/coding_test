word = input().lower()
cro = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
for c in cro:
    word = word.replace(c, "*").strip()
print(len(word))
