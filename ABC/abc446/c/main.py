import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    for _ in range(int(input())):
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        tamago = deque([])
        for i in range(n):
            tamago.append((i + 1, a[i]))

            while b[i] > 0:
                day, cnt = tamago[0]
                if cnt <= b[i]:
                    b[i] -= cnt
                    tamago.popleft()
                else:
                    tamago[0] = (day, cnt - b[i])
                    b[i] = 0

            while len(tamago) != 0 and tamago[0][0] + d <= i + 1:
                tamago.popleft()

        ans = 0
        while tamago:
            _, cnt = tamago.pop()
            ans += cnt
        print(ans)


if __name__ == "__main__":
    main()
