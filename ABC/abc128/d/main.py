import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, k = map(int, input().split())
    v = list(map(int, input().split()))

    ans = 0
    for a in range(k + 1):
        for b in range(k + 1):
            if a + b > k or a + b > n:
                continue
            d = deque(v)
            hand = []
            for _ in range(a):
                if d:
                    hand.append(d.pop())
            for _ in range(b):
                if d:
                    hand.append(d.popleft())
            cd = k - a - b
            hand.sort(reverse=True)
            for _ in range(cd):
                if hand and hand[-1] < 0:
                    hand.pop()
            ans = max(ans, sum(hand))

    print(ans)


if __name__ == "__main__":
    main()
