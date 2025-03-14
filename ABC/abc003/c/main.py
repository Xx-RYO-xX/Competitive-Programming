import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    r = sorted(map(int, input().split()))

    ans = 0.0
    for i in range(n-k, n):
        ans = (r[i]+ans)/2
    
    print(ans)

if __name__ == '__main__':
    main()
