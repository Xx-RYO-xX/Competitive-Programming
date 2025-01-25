import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(m):
        a.append(int(input()))
    
    thread = set(range(1, n+1))
    
    ans = []
    
    for i in range(m)[::-1]:
        if a[i] in thread:
            ans.append(a[i])
            thread.remove(a[i])
    
    ans += sorted(thread)

    print(*ans, sep="\n")


if __name__ == '__main__':
    sys.exit(main())
