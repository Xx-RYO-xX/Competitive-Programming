import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())

    tou_bangou = defaultdict(list)
    for _ in range(n):
        s, t = map(int, input().split())
        tou_bangou[t].append(s)

    for i in range(10**4):
        bangou = str(i).zfill(4)
        print(bangou)

if __name__ == '__main__':
    main()
