import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    shift = 0
    accm = [0] * (n + 1)
    for i in range(n):
        accm[i + 1] = accm[i] + a[i]

    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, c = map(int, query.split())
            shift = (shift + c) % n
        else:
            num, l, r = map(int, query.split())

            ll = (shift + l - 1) % n
            rr = (shift + r - 1) % n
            ans = 0
            if ll <= rr:
                ans = accm[rr + 1] - accm[ll]
            else:
                ans = (accm[n] - accm[ll]) + accm[rr + 1]
            print(ans)


if __name__ == "__main__":
    main()
