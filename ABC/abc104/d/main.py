import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    n = len(s)
    acqq = [[] for _ in range(n)]
    acqq[0].append(0)
    for i in range(1, n):
        acqq[i].append(acqq[i - 1][0] + (1 if s[i - 1] == "A" else 0))

    acqq[-1].append(0)
    for i in range(n - 1)[::-1]:
        acqq[i].append(acqq[i + 1][1] + (1 if s[i + 1] == "C" else 0))

    acqq[0].append(0)
    for i in range(1, n):
        acqq[i].append(acqq[i - 1][2] + (1 if s[i - 1] == "?" else 0))

    acqq[-1].append(0)
    for i in range(n - 1)[::-1]:
        acqq[i].append(acqq[i + 1][3] + (1 if s[i + 1] == "?" else 0))

    ans = 0
    MOD = 10**9 + 7
    for i in range(1, n - 1):
        if s[i] == "B" or s[i] == "?":
            acnt, ccnt, qb, qa = acqq[i]
            ans += (
                acnt
                * ccnt
                * (pow(3, qb, MOD) if qb > 0 else 1)
                * (pow(3, qa, MOD) if qa > 0 else 1)
            ) % MOD
            ans += (
                qa
                * qb
                * (pow(3, qb - 1, MOD) if qb > 0 else 1)
                * ((pow(3, qa - 1, MOD)) if qa > 0 else 1)
            ) % MOD
            ans += (
                acnt
                * qa
                * (pow(3, qb, MOD) if qb > 0 else 1)
                * (pow(3, qa - 1, MOD) if qa > 0 else 1)
            ) % MOD
            ans += (
                qb
                * ccnt
                * (pow(3, qb - 1, MOD) if qb > 0 else 1)
                * (pow(3, qa, MOD) if qa > 0 else 1)
            ) % MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
