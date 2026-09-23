nums = []
cnt = 0
while True:
    try:
        flag = True
        n = int(input())
        cnt += 1
        if cnt == 1:
            nums.append(n)
        else:
            for i, num in enumerate(nums):
                if n > num:
                    continue
                else:
                    # print(f"index: {i}, {n}")
                    nums.insert(i, n)
                    flag = False
                    break
            if flag:
                nums.append(n)
        """
        for i in nums:
            print(i, end=" ")
        print()
        """

        if cnt % 2 == 1:
            print(nums[cnt // 2])
        else:
            print((nums[cnt // 2 - 1] + nums[cnt // 2]) // 2)

    except EOFError:
        break
