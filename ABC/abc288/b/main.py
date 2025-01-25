import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    
    print(*sorted(s[:k]), sep="\n")


if __name__ == '__main__':
    main()
