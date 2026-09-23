n = int(input())
nums = list(map(int, input().split()))

for i in nums:
    print(i, end=" ")
print()

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for i in nums:
    print(i, end=" ")
print()
