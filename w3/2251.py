n = int(input())
for i in range(n):
    s = input()
    # print(s)
    # chars = set(s)
    maxnum = int(0)
    ans = ""
    for char in set(s):
        # print(f"{char} {s.count(char)}")
        if s.count(char) > maxnum:
            maxnum = s.count(char)
            ans = char

    print(ans)
