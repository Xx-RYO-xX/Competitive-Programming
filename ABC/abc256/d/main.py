import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    l_r = defaultdict(int)
    for i in range(n):
        l, r = map(int, input().split())
        l_r[l] = max(l_r[l], r)
    
    l_lst = sorted(l_r)
    ans = [[l_lst[0], l_r[l_lst[0]]]]
    for l in l_lst[1:]:
        lb, rb = ans[-1]
        r = l_r[l]
        if rb < l:
            ans.append([l, r])
        else:
            if rb < r:
                ans[-1][1] = r
    
    for a in ans:
        print(*a)

if __name__ == '__main__':
    sys.exit(main())
