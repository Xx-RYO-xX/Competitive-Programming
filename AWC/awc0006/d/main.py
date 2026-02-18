import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import time

    start = time.time()
    n, m = map(int, input().split())
    lr = []
    for _ in range(m):
        l, r = map(int, input().split())
        lr.append((l, r))
    lr.sort(key=lambda x: (x[0], -x[1]))

    if lr[0][0] != 1:
        print(-1)
        return

    right = lr[0][1]
    ans = 1
    i = 1
    while right < n:
        new_right = right
        for j in range(i, m):
            if lr[j][0] <= right + 1:
                if new_right < lr[j][1]:
                    new_right = lr[j][1]
                    i = j
            else:
                break
        if new_right == right or new_right <= right:
            print(-1)
            return
        right = new_right
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
