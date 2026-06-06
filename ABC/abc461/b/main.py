import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    for i in range(1, n + 1):
        if i != b[a[i]]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
