import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    s = input()

    if int(s) % 8 == 0:
        print("Yes")
        return

    if len(s) == 2 and int(s[1] + s[0]) % 8 == 0:
        print("Yes")
        return

    cnt = Counter(s)

    for i in range(112, 1000, 8):
        if len(Counter(str(i)) - cnt) == 0:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
