def find_carry(a, b):
    a0 = ["0"] * (10 - len(a)) + list(a)
    b0 = ["0"] * (10 - len(b)) + list(b)
    # print(a0)
    # print(b0)

    ans = 0
    last_carry = 0
    for i in range(9, 0, -1):
        na, nb = int(a0[i]), int(b0[i])
        if na + nb + last_carry >= 10:
            ans += 1
            last_carry = 1
        else:
            last_carry = 0

    return ans


while True:
    a, b = input().split()
    c, d = int(a), int(b)
    if c == 0 and d == 0:
        break
    ans = find_carry(a, b)
    if ans == 0:
        print("No carry operation.")
    elif ans == 1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")
