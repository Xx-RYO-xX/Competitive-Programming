import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input().lower()

    moji1 = False
    moji2 = False
    for S in s:
        if moji1 and moji2 and S == t[2]:
            print("Yes")
            return

        elif moji1 and not moji2 and S == t[1]:
            moji2 = True

        elif not moji1 and S == t[0]:
            moji1 = True

    if moji1 and moji2 and t[2] == "x":
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    main()
