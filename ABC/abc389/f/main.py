import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    lr = []
    for _ in range(n):
        l, r = map(int, input().split())
        lr.append((l, r))
        
    q = int(input())
    for _ in range(q):
        x = int(input())
        for l, r in lr:
            if l <= x <= r:  
                x += 1
        print(x)


if __name__ == '__main__':
    sys.exit(main())
