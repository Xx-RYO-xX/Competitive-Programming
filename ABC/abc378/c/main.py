import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    
    chokudai = defaultdict(lambda: -1)
    b = []
    for i in range(n):
        b.append(chokudai[a[i]])
        chokudai[a[i]] = i+1
    
    print(*b)


if __name__ == '__main__':
    main()
