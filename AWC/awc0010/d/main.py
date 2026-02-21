import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    sorted_h = sorted(h, reverse=True)
    bakuha = defaultdict(int)
    i = 0
    for i in range(k):
        bakuha[sorted_h[i]] += 1

    ans = 0
    for i in range(n):
        if h[i] in bakuha and bakuha[h[i]] > 0:
            ans += 1
            bakuha[h[i]] -= 1
        else:
            ans += h[i]

    print(ans)


if __name__ == "__main__":
    main()
