n = int(input())
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    nums.reverse()
    stack = []
    target = n
    for num in nums:
        # print(num)
        if num == target:
            target -= 1
            continue
        else:
            while len(stack) != 0 and stack[-1] == target:  # forget len(stack) != 0
                target -= 1
                stack.pop()
                continue
        stack.append(num)

    while len(stack) != 0 and stack[-1] == target:  # forget this part
        target -= 1
        stack.pop()
        continue

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
