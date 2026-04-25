import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())

    ans = 0
    for h1 in range(h):
        for h2 in range(h1, h):
            for w1 in range(w):
                for w2 in range(w1, w):
                    masu = True
                    for i in range(h1, h2 + 1):
                        for j in range(w1, w2 + 1):
                            if s[i][j] != s[h1 + h2 - i][w1 + w2 - j]:
                                masu = False

                    ans += masu
    print(ans)


if __name__ == "__main__":
    main()
