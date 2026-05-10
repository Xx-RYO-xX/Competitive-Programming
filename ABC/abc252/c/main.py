import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(list(input()))

    ans = float("inf")
    for i in range(10):
        time = set()
        for j in range(n):
            t = s[j].index(str(i))
            while t in time:
                t += 10
            time.add(t)
        ans = min(ans, max(time))

    print(ans)


if __name__ == "__main__":
    main()
