import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import re
    s = re.split("[^ACGT]", input())
    print(len(max(s, key=len)))


if __name__ == '__main__':
    main()
