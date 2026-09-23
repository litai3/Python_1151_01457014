n, m = map(int, input().split())
nums = list(map(int, input().split()))
l = len(nums)
flag = 0  # where change
for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        flag = i + 1
        break


def bsearch(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


for i in range(m):
    flag1 = False  # is found?
    t = int(input())
    if t < nums[0]:
        print(bsearch(nums, t, flag, l - 1))
    else:
        print(bsearch(nums, t, 0, flag - 1))
