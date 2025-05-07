import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from itertools import product
    
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    anim_to_zoo = defaultdict(set)
    for i in range(1, m+1):
        ka = list(map(int, input().split()))
        for a in ka[1:]:
            anim_to_zoo[i].add(a)
    # print(anim_to_zoo)
    
    ans = float("inf")
    for visit in product(range(3), repeat=n):
        cost = sum(visit[i]*c[i] for i in range(n))
        cond = True
        for anim in range(1, m+1):
            count = 0
            for zoo in anim_to_zoo[anim]:
                count += visit[zoo-1]  
            if count < 2:
                cond = False
                break
        if cond:
            ans = min(ans, cost)
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
