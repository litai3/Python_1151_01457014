stus = {}


def add_stu(stu):
    a, b, c = stu
    stus[a] = (b, c)


n = int(input())
while n > 0:
    stu = input().strip().split()
    add_stu(stu)
    n -= 1

n = int(input())
while n > 0:
    id = input().strip()
    stu = stus.get(id, 0)
    if stu != 0:
        name, grade = stu
        print(f"{name} {grade}")
    else:
        print("Not found")

    n -= 1
