def cal(a, b, D):
    x1, y1, z1, p1 = a
    x2, y2, z2, p2 = b
    dis = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 + abs(z1 - z2) ** 2
    if dis <= D and p1 != p2:
        return True
    else:
        return False


n, D = map(int, input().split())
nodes = []
for i in range(n):
    nodes.append(tuple(map(int, input().split())))

interfere = set()

for i in range(n):
    for j in range(i + 1, n):
        node1 = nodes[i]
        node2 = nodes[j]
        flag = cal(node1, node2, D)
        if flag:
            interfere.add(tuple(sorted((node1, node2))))
# 1. 2 tuple 可以直接用sorted
# 2. set 用add

"""
# swap and sort
del_index = []
for i in range(len(ans)):  # a, b is tuple
    a = ans[i][0]
    b = ans[i][1]
    for j in range(4):
        if a[j] > b[j]:
            del_index.append(i)
            ans.append((b, a))

for i in del_index:
    del ans[i]
"""
ans = sorted(list(interfere))
cnt = len(ans)

if cnt == 0:
    print("Interference Pairs: 0")
else:
    print(f"Interference Pairs: {cnt}")
    for i in ans:
        a, b = i  # 2 turple
        print(f"{a} <-> {b}")

"""
5 25
0 0 0 10
0 3 4 20
10 10 10 30
0 0 2 10
0 0 1 50
"""
