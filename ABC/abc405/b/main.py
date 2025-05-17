import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    seta = set(a)
    for x in range(1, m+1):
        if x not in seta:
            print(0)
            return
    pos = {}
    for i, v in enumerate(a):
        if 1 <= v <= m and v not in pos:
            pos[v] = i

    lens = max(pos.values())+1

    print(n-(lens- 1))


if __name__ == '__main__':
    sys.exit(main())
