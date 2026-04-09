import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    rokkotu = []
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
        rokkotu.append(set())
    m = int(input())
    tango = []
    for __ in range(m):
        s = input()
        tango.append(s)
        for i in range(n):
            a, b = ab[i]
            if a == len(s):
                rokkotu[i].add(s[b - 1])

    # print(rokkotu)
    for s in tango:
        if len(s) == n:
            for i in range(len(s)):
                if s[i] not in rokkotu[i]:
                    print("No")
                    break
            else:
                print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
