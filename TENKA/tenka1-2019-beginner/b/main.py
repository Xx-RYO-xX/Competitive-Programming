import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(input())
    k = int(input())
    
    for i in range(n):
        if s[i] != s[k-1]:
            s[i] = "*"
    
    print("".join(s))


if __name__ == '__main__':
    sys.exit(main())
