import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split())) 

    ans = -1

    for i in range(101):
        sums = a + [i]
        sums.sort() 
        if sum(sums[1:n-1]) >= x:
            ans = i
            break 

    print(ans)


if __name__ == '__main__':
    sys.exit(main())
