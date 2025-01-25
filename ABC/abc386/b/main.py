import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    i = 0
    ans = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == '0' and s[i+1] == '0':
            ans += 1
            i += 2
        else:
            ans += 1
            i += 1
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
