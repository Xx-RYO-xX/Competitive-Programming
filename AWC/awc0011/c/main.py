import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for A in a:
        if A & k == A:
            ans |= A
            cnt += 1
    print(cnt if ans == k and cnt != 0 else -1)


if __name__ == "__main__":
    main()
