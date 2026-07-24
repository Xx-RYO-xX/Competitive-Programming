import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sympy.ntheory.generate import primerange

    n = int(input())

    prime = list(primerange(int((n / (4 * 3)) ** (1 / 2)) + 1))
    # print(len(prime))

    # print(prime)
    ans = 0
    for i in range(len(prime) - 2):
        for j in range(i + 1, len(prime) - 1):
            # print(i, j)
            a, b = prime[i], prime[j]
            ok = j
            ng = len(prime)
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if a**2 * b * prime[mid] ** 2 <= n:
                    ok = mid
                else:
                    ng = mid
            ans += ok - j
            if ok - j == 0:
                break
    print(ans)


if __name__ == "__main__":
    main()
