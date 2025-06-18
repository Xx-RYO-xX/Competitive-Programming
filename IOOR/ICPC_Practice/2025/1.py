import sys


def input():return sys.stdin.readline().rstrip()


def main():
    while True:
        n, m = map(int, input().split())
        if n == m == 0: return
        p = []
        for _ in range(m):
            p.append(list(map(int, input().split())))
        ans = 0
        for j in range(n):
            anst = 0
            for i in range(m):
                anst += p[i][j]
            ans = max(ans, anst)
        print(ans)    


if __name__ == '__main__':
    main()
