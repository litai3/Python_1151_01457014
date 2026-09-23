n = int(input())
if n <= 1:
    print("Invalid input")
else:

    for i in range(n):
        print(" " * (n - i - 1) + "*", end="")
        if i != 0:
            print(" " * ((i - 1) * 2 + 1) + "*", end="")
        print()

    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*", end="")
        if i != 0:
            print(" " * ((i - 1) * 2 + 1) + "*", end="")
        print()
