import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ai_max = [a[0]]
    for i in range(1, n):
        ai_max.append(max(ai_max[-1], a[i]))

    # print(ai_max)

    aa = []
    for i in range(n):
        # print(a[i], ai_max[i])
        aa.append(max(a[i], ai_max[i]))
        if i != n - 1:
            ai_max[i + 1] = max(aa[-1], ai_max[i + 1])
        # print(aa)

    ans = 0
    for i in range(n):
        ans += aa[i] - a[i]

    print(ans)


if __name__ == "__main__":
    main()
