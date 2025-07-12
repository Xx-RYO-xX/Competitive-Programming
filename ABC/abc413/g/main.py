import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    h, w, k = map(int, input().split())
    batu = set()
    up = []
    down = []
    left =[]
    right = []
    for _ in range(k):
        r, c = map(int, input().split())
        batu.add((r, c))
        if r == 1:
            up.append((r, c))
        if r == h:
            down.append((r, c))
        if c == 1:
            left.append((r, c))
        if c == w:
            right.append((r, c))
    
    



if __name__ == '__main__':
    main()
