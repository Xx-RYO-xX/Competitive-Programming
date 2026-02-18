import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    def can(x):
        track = 0
        cut = 0
        for aa in a:
            track += aa
            if track >= x:
                track = 0
                cut += 1
                if cut == k:
                    return True
        return False

    left = 0
    right = sum(a)
    while left <= right:
        mid = (left + right) // 2
        if can(mid):
            left = mid + 1
        else:
            right = mid - 1

    print(right)


if __name__ == "__main__":
    main()
