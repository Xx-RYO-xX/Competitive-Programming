import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    
    shop = []
    for _ in range(m):
        a, b = map(int, input().split())
        shop.append([a, b])
    

    koukann = []
    for a, b in shop:
        sa = a-b
        if sa <= 0:
            continue
        koukann.append((sa, a))

    ans = 0
    koukann.sort()
    for sa, a in koukann:
        if n < a:
            continue
        get = (n-a)//sa+1
        ans += get
        n -= get*sa
    print(ans)


if __name__ == '__main__':
    main()
