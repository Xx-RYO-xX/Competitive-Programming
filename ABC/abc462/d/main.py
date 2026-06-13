import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, d = map(int, input().split())
    kukan = [0] * (10**6 + 2)
    for _ in range(n):
        s, t = map(int, input().split())
        if t - s < d:
            continue
        kukan[s] += 1
        kukan[t - d + 1] -= 1

    ans = 0
    accm = [0]
    for K in kukan:
        accm.append(accm[-1] + K)
        ans += (accm[-1] * (accm[-1] - 1)) // 2

    print(ans)


if __name__ == "__main__":
    main()
