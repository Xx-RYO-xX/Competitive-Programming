import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    ans = 0
    for i in range(1, n+1):
        num = i
        anst = 0
        while num % 2 == 0:
            num /= 2
            anst += 1
        ans = max(ans, anst)
    
    print(ans)


if __name__ == '__main__':
    main()
