n, m = map(int, input().split())
nums = list(map(int, input().split()))
flag = 0  # where change
for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        flag = i + 1
        break
def binary_search(arr, target):
    
for i in range(m):
    flag1 = False  # is found?
    t = int(input())
    if t < nums[0]:
        for j, num in enumerate(nums[flag:], start=flag):  # start from flag
            if t == num:
                print(j)
                flag1 = True
                break
        if flag1 == False:
            print(-1)
    else:
        for j, num in enumerate(nums[:flag]):  # start from 0
            if t == num:
                print(j)
                flag1 = True
                break

        if flag1 == False:
            print(-1)
