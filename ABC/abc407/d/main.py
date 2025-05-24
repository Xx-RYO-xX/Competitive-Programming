import sys


def input(): return sys.stdin.readline().rstrip()


def bit_full_search(lst, n):
    ans = []
    for i in range(2 ** n):
        s_u_m = []
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m.append(lst[j])
        ans.append(s_u_m)

    return ans


def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))

    n = h*w
    maxs = (1<<n)-1
    
    from functools import cache
    @cache
    def can_tile(cover):
        if cover == 0:
            return True
    
        i = (cover & -cover).bit_length()-1
        
        x0, y0 = divmod(i, w)
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = x0+dx, y0+dy
            
            if 0 <= nx < h and 0 <= ny < w:
                j = nx* w+ny
                if (cover>>j) & 1:
                    m2 = cover&~(1<<i)&~(1<<j)
                    if can_tile(m2):
                        return True
        
        return False


    ans = 0
    for hole_lst in bit_full_search(list(range(n)), n):
        holes = 0
        for idx in hole_lst:
            holes |= 1 << idx
        cover = maxs ^ holes

        if not can_tile(cover):
            continue

        anst = 0
        for idx in hole_lst:
            anst ^= a[idx//w][idx%w]

        ans = max(ans, anst)

    print(ans)


if __name__ == '__main__':
    sys.exit(main())
