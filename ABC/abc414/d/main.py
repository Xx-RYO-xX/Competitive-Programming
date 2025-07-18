import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    x = sorted(set(map(int, input().split())))
    
    len_x = len(x)
    if len(x) <= m:
        print(0)
        return

    x_sa = sorted(((x[i]-x[i-1], i) for i in range(1, len_x)), reverse=True)

    x_split = sorted(i for sa, i in x_sa[:m-1])
    ans = 0
    start = 0
    for s in x_split:
        end = s-1
        ans += x[end]-x[start]
        start = s
    end = len_x-1
    ans += x[end]-x[start]

    print(ans)


if __name__ == '__main__':
    main()
