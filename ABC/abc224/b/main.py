import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    for i1 in range(h):
        for i2 in range(i1 + 1, h):
            for j1 in range(w):
                for j2 in range(j1 + 1, w):
                    if a[i1][j1] + a[i2][j2] > a[i2][j1] + a[i1][j2]:
                        print("No")
                        return

    print("Yes")


if __name__ == "__main__":
    main()
