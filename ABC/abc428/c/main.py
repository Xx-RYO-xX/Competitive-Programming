import sys


def input():
    return sys.stdin.readline().rstrip()


def good(c):
    return 1 if c == "(" else -1


def main():
    from collections import deque

    q = deque()
    minus_cnt = 0
    accm = deque([0])
    ans = 0
    for _ in range(int(input())):
        query = input()
        if query[0] == "1":
            que, c = query.split()
            q.append(c)
            ans += good(c)

            nex = accm[-1] + good(c)
            if nex < 0:
                minus_cnt += 1
            accm.append(nex)
        else:
            c = q.pop()
            ans -= good(c)

            if accm.pop() < 0:
                minus_cnt -= 1

        print("Yes" if ans == 0 and minus_cnt == 0 else "No")


if __name__ == "__main__":
    main()
