import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    for i in range(1, n):
        for l in range(1, n + 1):
            if l + i <= n:
                if s[l - 1] == s[l - 1 + i]:
                    print(l - 1)
                    break
            else:
                print(l - 1)
                break


if __name__ == "__main__":
    main()
