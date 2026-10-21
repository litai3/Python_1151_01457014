class notnumber(Exception):
    pass


class floatnumber(Exception):
    pass


class outofrange(Exception):
    pass


def check(num):  # 原本的寫法會把負數當小數
    try:
        value = float(num)
    except ValueError:
        raise notnumber

    if not value.is_integer():
        raise floatnumber

    value = int(value)
    if value < 0 or value > 50:
        raise outofrange
    return value


n = 0
ans = 0
try:
    ans = input()
    ans = check(ans)

    while True:
        try:
            guess = input()
            n += 1
            guess = check(guess)

            if guess > ans:
                print("You are too high!")
            elif guess < ans:
                print("You are too low!")
            else:
                print("You got it!")
                break
        except notnumber:
            print("Error: please enter a number")
        except floatnumber:
            print("Error: please enter an integer")
        except outofrange:
            print("Error: number out of range")

except notnumber:
    print("Error: please enter a number")
except floatnumber:
    print("Error: please enter an integer")
except outofrange:
    print("Error: number out of range")
finally:
    print(f"You guessed {n} times.")
