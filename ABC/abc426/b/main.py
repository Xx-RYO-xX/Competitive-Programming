import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    s = input()

    moji1, moji2 = set(s)

    if s.count(moji1) < s.count(moji2):
        print(moji1)
    else:
        print(moji2)


if __name__ == "__main__":
    main()
