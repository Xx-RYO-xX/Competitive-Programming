import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()

    for i in range(len(s)):
        if s[i] != t[i]:
            print(i + 1)
            return

    print(len(t))


if __name__ == "__main__":
    main()
