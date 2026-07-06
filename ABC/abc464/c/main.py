import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, m = map(int, input().split())
    color = defaultdict(int)
    day = defaultdict(list)
    for _ in range(n):
        a, d, b = map(int, input().split())
        color[a] += 1
        day[d].append((a, b))

    for j in range(1, m + 1):
        if j not in day:
            print(len(color))
            continue
        for a, b in day[j]:
            color[a] -= 1
            color[b] += 1
            if color[a] == 0:
                color.pop(a)
        print(len(color))


if __name__ == "__main__":
    main()
