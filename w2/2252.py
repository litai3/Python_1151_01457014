n = int(input())
if n <= 0:
    print("Invalid input")

cnt = 0
for i in range(n):
    for j in range(i + 1):
        cnt += 1
        print(cnt, end=" ")
    print()
