import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import sympy
    import bisect

    n = int(input())

    prime = [i for i in sympy.sieve.primerange(10**6)]

    ans = 0
    for i in range(len(prime)):
        q = prime[i]
        left = 0
        right = i
        p = prime[left]
        if p * (q**3) <= n:
            # print(q)
            while left < right:
                mid = (left + right) // 2
                p = prime[mid]
                if p * (q**3) <= n:
                    left = mid + 1
                else:
                    right = mid

            ans += left

    print(ans)


if __name__ == "__main__":
    main()
