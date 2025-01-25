import sys


def input():return sys.stdin.readline().rstrip()


def main():
    m = int(input())
    
    ans = []
    for i in range(10, -1, -1):
        p = 3 ** i
        while m >= p and len(ans) < 20:
            ans.append(i)
            m -= p
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
