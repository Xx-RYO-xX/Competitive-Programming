import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    for A in a:
        mod = A % 6
        match mod:
            case 0:
                ans += 3
            case 1:
                ans += 0
            case 2:
                ans += 1
            case 3:
                ans += 0
            case 4:
                ans += 1
            case 5:
                ans += 2
    print(ans)

if __name__ == '__main__':
    main()
