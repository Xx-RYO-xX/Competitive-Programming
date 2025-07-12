import sys


def input():return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        
        l_len = len(p)
        for k in range(0, n+1):
            kukan = 1 << k
            for i in range(0, l_len, kukan):
                s = p[i:i+kukan]
                s_rev = s[::-1]
                if s_rev < s:
                    p[i:i+kukan] = s_rev
        print(*p)


if __name__ == '__main__':
    main()
