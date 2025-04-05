import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = ([a[i]%2 for i in range(n)].count(0), 2)
    # print(ans)
    for j in range(3, 1001):
        count = 0
        for i in range(n):
            if a[i] % j == 0:
                count += 1
        ans = max(ans, (count, j))
    
    print(ans[1])

if __name__ == '__main__':
    main()
