import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if sorted([a[i], b[j], c[k]]) == [4, 5, 6]:
                    ans += 1

    print(ans / 216)


if __name__ == "__main__":
    main()
