import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    ab = []
    med_count = 0
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
        med_count += b
    
    if med_count <= k:
        print(1)
        exit()
    
    ab.sort()
    
    ans = 0
    before_a = 0
    for AB in ab:
        a, b = AB
        ans += a-before_a
        med_count -= b
        if med_count <= k:
            print(ans+1)
            exit()
        before_a = a


if __name__ == '__main__':
    main()
