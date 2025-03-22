import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s = Counter(s)
    print("AC x", s["AC"])
    print("WA x", s["WA"])
    print("TLE x", s["TLE"])
    print("RE x", s["RE"])


if __name__ == '__main__':
    main()
