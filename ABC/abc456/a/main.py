import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    sai = set()
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                sai.add(i + j + k)

    print("Yes" if x in sai else "No")


if __name__ == "__main__":
    main()
