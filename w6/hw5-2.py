def def_G(N):
    G = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            G += GCD(i, j)  # math.gcd(i, j)
    return G


def GCD(i, j):
    if j == 0:
        return i
    return GCD(j, i % j)


while True:
    N = int(input().strip())
    if N == 0:
        break
    ans = def_G(N)
    print(ans)
