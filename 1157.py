word = input().upper()
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
dic = sorted(dic.items(), key=lambda x: x[1])
if len(dic) > 1 and dic[-1][1] == dic[-2][1]:
    print("?")
else:
    print(dic[-1][0])
