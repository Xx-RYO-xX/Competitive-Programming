import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    c = []
    for _ in range(h):
        ct = list(input())
        c.append(ct)

    while True:
        if all([ctt == "." for ctt in c[0]]):
            c.pop(0)
        else:
            break

    while True:
        if all([ctt == "." for ctt in c[-1]]):
            c.pop()
        else:
            break

    while True:
        # print(*c, sep="\n")
        # print()
        for j in range(len(c)):
            if c[j][0] == "#":
                break
        else:
            for j in range(len(c)):
                c[j].pop(0)
            continue
        break

    while True:
        # print(*c, sep="\n")
        # print()
        for j in range(len(c)):
            if c[j][-1] == "#":
                break
        else:
            for j in range(len(c)):
                c[j].pop()
            continue
        break

    for C in c:
        print(*C, sep="")


if __name__ == "__main__":
    main()
