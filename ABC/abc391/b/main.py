import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    t = []
    for _ in range(m):
        t.append(input())
    
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            cond = True
            for k in range(m):
                for l in range(m):
                    if s[i+k][j+l] != t[k][l]:
                        cond = False
                        break
                if not cond:
                    break
            if cond:
                print(i+1, j+1)
                return


if __name__ == '__main__':
    sys.exit(main())
