s = input().lower().split()
dic = dict()
for i in s:
    if i not in dic:
        dic[f"{i}"] = 1
    else:
        dic[f"{i}"] += 1
for k, v in dic.items():
    print(f"{k} {v}")
