class ivalidformat(Exception):
    pass


class ivalidscore(Exception):
    pass


def check(data):
    if len(data) != 2 or data[1] == "" or data[0] == "":
        raise ivalidformat
    try:
        score = float(data[1])
    except ValueError:
        # print("X")
        raise ivalidscore

    if score.is_integer():
        score = int(score)
        # print(f"score {score}")
        if score >= 0 and score <= 100:
            return score
        else:
            # print("Y")
            raise ivalidscore
    else:
        # print("Z")
        raise ivalidscore


n = int(input())
cnt = 0
sum = 0
for i in range(n):
    try:
        data = input().split(",")
        score = check(data)
        name = data[0]
        cnt += 1
        sum += score
        print("OK")
    except ivalidformat:
        print("Error: invalid data format")
    except ivalidscore:
        print("Error: invalid score")

if cnt == 0:
    print("No valid scores")
else:
    avg = sum / float(cnt)
    avg = round(avg, 2)
    result = f"{avg:.2f}"  # 強制輸出兩位小數
    print(f"Average score: {result}")
