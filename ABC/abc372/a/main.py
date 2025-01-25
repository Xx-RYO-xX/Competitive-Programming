import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    ans = ""
    for i in range(len(s)):
        if s[i] != ".":
            ans += s[i]
    
    print(ans)


if __name__ == '__main__':
    main()
