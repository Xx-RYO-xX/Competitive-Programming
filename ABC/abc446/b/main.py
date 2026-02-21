import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    ju = set(range(1, m + 1))
    for _ in range(n):
        l = int(input())
        x = list(map(int, input().split()))
        for xx in x:
            if xx in ju:
                ju.remove(xx)
                print(xx)
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
