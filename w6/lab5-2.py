def cola(n):
    ans = 0
    empty = 0
    while n != 0:
        ans += n
        empty += n
        n = empty // 3
        empty = empty % 3
    if empty == 2:
        ans += 1
    return ans


while True:
    try:
        n = int(input())
    except EOFError:
        break
    ans = cola(n)
    print(ans)
