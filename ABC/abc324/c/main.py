import sys


def input():
    return sys.stdin.readline().rstrip()


def check(s, t):
    if len(s) > len(t):
        return check(t, s)

    if len(s) < len(t) - 1:
        return False

    i, j, cnt = 0, 0, 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            cnt += 1
            if cnt > 1:
                return False
            if len(s) == len(t):
                i += 1
            j += 1

    return True


def main():
    n, t = input().split()
    ans = []
    for i in range(1, int(n) + 1):
        s = input()
        if check(s, t):
            ans.append(i)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
