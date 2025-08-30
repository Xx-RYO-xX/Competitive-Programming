import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))

    snuke = "snuke"

    for i in range(h):
        for j in range(w):

            if j + 4 < w:
                yoko = "".join(s[i][j + k] for k in range(5))
                if yoko == snuke:
                    for k in range(5):
                        print(i + 1, j + k + 1)
                    return
                elif yoko == snuke[::-1]:
                    for k in range(5):
                        print(i + 1, j + 1 + (4 - k))
                    return

            if i + 4 < h:
                tate = "".join(s[i + k][j] for k in range(5))
                if tate == snuke:
                    for k in range(5):
                        print(i + k + 1, j + 1)
                    return
                elif tate == snuke[::-1]:
                    for k in range(5):
                        print(i + 1 + (4 - k), j + 1)
                    return

            if i + 4 < h and j + 4 < w:
                naname = "".join(s[i + k][j + k] for k in range(5))
                if naname == snuke:
                    for k in range(5):
                        print(i + k + 1, j + k + 1)
                    return
                elif naname == snuke[::-1]:
                    for k in range(5):
                        print(i + 1 + (4 - k), j + 1 + (4 - k))
                    return

            if i + 4 < h and j - 4 >= 0:
                naname2 = "".join(s[i + k][j - k] for k in range(5))
                if naname2 == snuke:
                    for k in range(5):
                        print(i + k + 1, j - k + 1)
                    return
                elif naname2 == snuke[::-1]:
                    for k in range(5):
                        print(i + 1 + (4 - k), j + 1 - (4 - k))
                    return


if __name__ == "__main__":
    main()
