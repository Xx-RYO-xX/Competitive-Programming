import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n = int(input())
    s = input()

    guuki = 0
    ans = deque([])
    for i in range(n):
        if guuki % 2 == 0:
            ans.append(i + 1)
        else:
            ans.appendleft(i + 1)
        guuki += s[i] == "o"

    anst = ans if guuki % 2 == 0 else reversed(ans)
    print(*anst)


if __name__ == "__main__":
    main()
