import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    l = int(input())
    c = set(map(int, input().split()))
    q = int(input())
    x = list(map(int, input().split()))

    ans = set()
    for A in a:
        for B in b:
            for C in c:
                ans.add(A + B + C)

    for X in x:
        print("Yes" if X in ans else "No")


if __name__ == "__main__":
    main()
