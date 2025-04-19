import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = set()
    for _ in range(n):
        tmp = list(map(int, input().split()))
        ans.add(tuple(tmp[1:]))
    
    print(len(ans))


if __name__ == '__main__':
    sys.exit(main())
