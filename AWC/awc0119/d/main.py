def main():
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())

    ec = []
    for _ in range(n):
        e, c = map(int, input().split())
        ec.append((e, c))
    d = sorted(map(int, input().split()), reverse=True)

    ec.sort(reverse=True)

    from collections import deque

    ec = deque(ec)
    d = deque(d)

    ans = 0
    while ec and d:
        e, c = ec.popleft()
        dd = d.popleft()
        if e >= dd:
            ans += 1
            c -= 1
        if c == 0:
            continue
        ec.appendleft((e, c))

    print(ans)


if __name__ == "__main__":
    main()
