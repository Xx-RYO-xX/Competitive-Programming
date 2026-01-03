import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    loop = set()
    while n != 1:
        loop.add(n)
        n = sum(int(num) ** 2 for num in str(n))
        if n in loop:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
