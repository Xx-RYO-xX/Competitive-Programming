import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()

    AZ = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    try:
        if (
            len(s) == 8
            and s[0] in AZ
            and s[-1] in AZ
            and 100000 <= int(s[1:-1]) <= 999999
        ):
            print("Yes")
        else:
            print("No")
    except:
        print("No")


if __name__ == "__main__":
    main()
