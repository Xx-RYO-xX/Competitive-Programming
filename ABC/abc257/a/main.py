import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    ans = ""
    for i in range(26):
        ans += chr(ord("A")+i)*n
    
    print(ans[x-1])


if __name__ == '__main__':
    main()
