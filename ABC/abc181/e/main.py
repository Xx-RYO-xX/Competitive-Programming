import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate

    n, m = map(int, input().split())
    h = sorted(map(int, input().split()))
    w = list(map(int, input().split()))

    h0 = []
    h1 = []
    for i in range(0, n, 2):
        if i != n - 1:
            h0.append(h[i + 1] - h[i])
        if i < n - 2:
            h1.append(h[i + 2] - h[i + 1])

    h0accm = [0] + list(accumulate(h0))
    h1accm = [0] + list(accumulate(h1))

    print(h0accm)
    print(h1accm)
    
    for W in w:
        


if __name__ == "__main__":
    main()
