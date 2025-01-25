import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, c1, c2 = input().split()
    s = input()
    ans = ""
    for S in s:
        if S != c1:
            ans += c2
        else:
            ans += S
    
    print(ans)


if __name__ == '__main__':
    main()
