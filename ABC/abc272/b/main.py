import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations
    n, m = map(int, input().split())
    hantei = list([False]*n for _ in range(n))
    for _ in range(m):
        kx = list(map(int, input().split()))
        for comb in combinations(kx[1:], 2):
            p1, p2 = comb
            p1 -= 1
            p2 -= 1
            
            hantei[p1][p1], hantei[p2][p2] = True, True
            hantei[p1][p2], hantei[p2][p1] = True, True
            
    if all(all(row) for row in hantei):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
