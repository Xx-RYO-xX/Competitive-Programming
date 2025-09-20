import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = []

    while n > 3:
        if n % 2 != 0:
            n -= 1
            ans.append("A")
        n //= 2
        ans.append("B")

    for i in range(n):
        ans.append("A")

    print(*ans[::-1], sep="")


if __name__ == "__main__":
    main()
