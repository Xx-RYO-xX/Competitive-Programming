import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())

    for i in range(h):
        pre = ""
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                pre += "#"
            else:
                pre += "."
        print(pre)


if __name__ == "__main__":
    main()
