import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, d = map(int, input().split())
    s = list(input())
    
    for i in range(n)[::-1]:
        # print(s)
        if s[i] == "@" and d != 0:
            s[i] = "."
            d -= 1
        if d == 0:
            break
    
    print(*s, sep="")


if __name__ == '__main__':
    main()
