import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y = map(int, input().split())
    a = [0] * 11
    a[1], a[2] = x, y

    for i in range(3, 11):
        s = str(a[i - 1] + a[i - 2])
        a[i] = int(s[::-1])

    print(a[10])


if __name__ == "__main__":
    main()
