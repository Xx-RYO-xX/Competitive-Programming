import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())

    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for i in range(h):
        for j in range(w):
            count = 0
            if s[i][j] == "#":
                # print(i, j)
                for d in direction:
                    di, dj = d
                    if 0 <= i + di < h and 0 <= j + dj < w:
                        if s[i + di][j + dj] == "#":
                            count += 1
                            # print(i + di, j + dj)
                            # print(count)
                            # print()

                if count == 0 or count == 1 or count == 3:
                    # print(count)
                    # print(i, j)
                    print("No")
                    return

    print("Yes")


if __name__ == "__main__":
    main()
