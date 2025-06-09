import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    h, w, n = map(int, input().split())
    masu = defaultdict(int)
    masu_default_key = []
    for _ in range(n):
        a, b = map(int, input().split())
        masu_default_key.append((a, b))
        masu[(a, b)] = 1
    
    ans = defaultdict(int)
    visited = set()
    
    for a, b in masu_default_key:
        for xm in range(3):
            for ym in range(3):
                x, y = a-xm, b-ym
                if (x, y) not in visited:
                    cnt = 0
                    for i in range(3):
                        for j in range(3):
                            if masu[(x, y)] == 1:
                                cnt += 1
                    ans[cnt] += 1
                    visited.add((x, y))

    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    sys.exit(main())
