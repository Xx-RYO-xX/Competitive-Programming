import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    s = list(input())
    
    ans = 0
    i = 0
    while i < n:
        if "".join(s[i:i+k]) == "O"*k:
            ans += 1
            i += k-1
        i += 1
    print(ans)


if __name__ == '__main__':
    main()
