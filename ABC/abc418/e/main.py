import sys



def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    from math import gcd

    n = int(input())
    xy_lst = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy_lst.append((x, y))
    
    
    hen_to_cnt = Counter()
    mid_cnt = Counter()
    
    for i in range(n):
        for j in range(i+1, n):
            p1 = xy_lst[i]
            p2 = xy_lst[j]
            
            x = p1[0]-p2[0]
            y = p1[1]-p2[1]

            if x == 0:
                hen = (0, 1)
            elif y == 0:
                hen = (1, 0)
            else:
                kiyaku = gcd(x, y)
                x //= kiyaku
                y //= kiyaku
                if x < 0:
                    x = -x
                    y = -y
                hen = (x, y)
    
            hen_to_cnt[hen] += 1
            
            mid = (p1[0]+p2[0], p1[1]+p2[1])
            mid_cnt[mid] += 1

    anst = 0
    for cnt in hen_to_cnt.values():
        anst += cnt*(cnt-1)//2
        
    heikousihenkei = 0
    for cnt in mid_cnt.values():
        heikousihenkei += cnt*(cnt-1)//2

    ans = anst-heikousihenkei
    print(ans)

if __name__ == '__main__':
    main()
