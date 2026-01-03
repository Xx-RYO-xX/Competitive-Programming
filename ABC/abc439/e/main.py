import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import bisect

    n = int(input())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))

    ab.sort(key=lambda x: (x[0], -x[1]))

    # https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
    LIS = [ab[0][1]]
    for i in range(1, n):
        if ab[i][1] > LIS[-1]:
            LIS.append(ab[i][1])
        else:
            LIS[bisect.bisect_left(LIS, ab[i][1])] = ab[i][1]

    print(len(LIS))


if __name__ == "__main__":
    main()
