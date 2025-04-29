import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import itertools
    n, m = map(int, input().split())
    takahashi = defaultdict(list)
    for _ in range(m):
        a, b, = map(int, input().split())
        takahashi[a].append(b)
        takahashi[a].sort()
        takahashi[b].append(a)
        takahashi[b].sort()
    
    aoki = defaultdict(list)
    for _ in range(m):
        c, d = map(int, input().split())
        aoki[c].append(d)
        aoki[c].sort()
        aoki[d].append(c)
        aoki[d].sort()

    for p in itertools.permutations(range(1, n+1)):
        cond = True
        for i in range(1, n+1):
            mapped = sorted(p[j-1] for j in takahashi[i])
            if mapped != sorted(aoki[p[i-1]]):
                cond = False
                break
        if cond:
            print("Yes")
            return

    print("No")
    
    
if __name__ == '__main__':
    main()
