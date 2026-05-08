import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = float("inf")
    for i in range(2 ** (n - 1)):
        kukan = set()
        for j in range(n - 1):
            bit = 2**j
            if (i // bit) % 2 == 1:
                kukan.add(j)
        anst = [0]
        for i in range(n):
            anst[-1] |= a[i]
            if i in kukan:
                anst.append(0)
        ANST = 0
        for at in anst:
            ANST ^= at
        ans = min(ans, ANST)

    print(ans)


if __name__ == "__main__":
    main()
