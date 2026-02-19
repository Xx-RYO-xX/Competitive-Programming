import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    lr = []
    for _ in range(m):
        l, r = map(int, input().split())
        lr.append((l, r))

    if m == 0:
        print(n)
        return

    lr = sorted(lr)
    llrr = [lr[0]]
    for i in range(1, m):
        ll, rr = llrr[-1]
        l, r = lr[i]
        if l <= rr + 1:
            if rr < r:
                llrr[-1] = (ll, r)
        else:
            llrr.append((l, r))

    day = 1
    for l, r in llrr:
        sun = l - day
        if n <= sun:
            print(day + n - 1)
            return
        n -= sun
        day = r + 1

    print(day + n - 1)


if __name__ == "__main__":
    main()
