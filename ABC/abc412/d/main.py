import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    
    n, m = map(int, input().split())
    g = set()
    for _ in range(m):
        a, b = map(int, input().split())
        g.add(tuple(sorted((a, b))))

    ans = float("inf")
    for perm in permutations(range(1, n+1)):
        gt = set()
        for i in range(n):
            gt.add(tuple(sorted((perm[i], perm[i-1]))))
        
        ans = min(ans, len(g^gt))
        if 6 <= n:
            for j in range(3, n-2):
                gt = set()
                p1 = perm[:j]
                p2 = perm[j:]
                for i in range(j):
                    gt.add(tuple(sorted((p1[i], p1[i-1]))))
                for i in range(n-j):
                    gt.add(tuple(sorted((p2[i], p2[i-1]))))
                # print(gt)
                ans = min(ans, len(g^gt))
    
    print(ans)

    


if __name__ == '__main__':
    main()
