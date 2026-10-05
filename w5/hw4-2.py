com = {
    "A": "A",
    "B": " ",
    "C": " ",
    "D": " ",
    "E": "3",
    "F": " ",
    "G": " ",
    "H": "H",
    "I": "I",
    "J": "L",
    "K": " ",
    "L": "J",
    "M": "M",
    "N": " ",
    "O": "O",
    "P": " ",
    "Q": " ",
    "R": " ",
    "S": "2",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "5",
    "1": "1",
    "2": "S",
    "3": "E",
    "4": " ",
    "5": "Z",
    "6": " ",
    "7": " ",
    "8": "8",
    "9": " ",
}


def mirr(s, sr):
    for i in range(len(s)):
        mirror_char = com.get(sr[i], " ")  # 避免Key error
        if s[i] == mirror_char:
            continue
        else:
            return False
    return True


def pali(s, sr):
    for i in range(len(s)):
        if s[i] == sr[i]:
            continue
        else:
            return False
    return True


try:
    while True:
        s = input().strip()
        sr = list(s)
        sr.reverse()
        flag1 = mirr(s, sr)
        flag2 = pali(s, sr)
        if flag1 and flag2:
            print(f"{s} -- is a mirrored palindrome.")
        elif flag1:
            print(f"{s} -- is a mirrored string.")
        elif flag2:
            print(f"{s} -- is a regular palindrome.")
        else:
            print(f"{s} -- is not a palindrome.")
        print("")
except EOFError:
    pass
