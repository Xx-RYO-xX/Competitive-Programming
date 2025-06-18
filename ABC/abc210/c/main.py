import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    
    candy = defaultdict(int)
    for i in range(k):
        candy[c[i]] += 1
    
    uresii = len(candy)
    for i in range(k, n):
        in_candy = c[i]
        out_candy = c[i-k]
        candy[in_candy] += 1
        candy[out_candy] -=1
        if candy[out_candy] == 0:
            candy.pop(out_candy)
        uresii = max(uresii, len(candy))
    
    print(uresii)

if __name__ == '__main__':
    main()
