import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = list(input().split())
    ans = set()
    for S in s:
        ss = ""
        for SS in S[::-1]:
            if SS == "@":
                ans.add(ss[::-1])
                ss = ""
            else:
                ss += SS
    ans.discard("")
    print(*sorted(ans), sep="\n")

if __name__ == '__main__':
    main()
