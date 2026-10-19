def sum_even(*nums):
    sum = 0
    for i in nums:
        if i % 2 == 0:
            sum += i
    return sum


while True:
    nums = input()
    if nums == "END":
        break
    nums = map(int, nums.split())
    ans = sum_even(*nums)
    print(ans)
