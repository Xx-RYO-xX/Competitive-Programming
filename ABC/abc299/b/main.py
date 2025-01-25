import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n, t = map(int, input().split())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))
    cr = defaultdict(lambda: (0, 0))
    p1c = c[0]
    for i in range(n):
        cr[c[i]] = (r[i], i+1) if cr[c[i]][0] < r[i] else cr[c[i]]
    
    if t in cr.keys():
        print(cr[t][1])
    else:
        print(cr[p1c][1])

if __name__ == '__main__':
    main()
