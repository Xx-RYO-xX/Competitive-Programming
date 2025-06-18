import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    
    count = [0]*n
    ans = []
    for X in x:
        if X >= 1:
            idx = X - 1
        else:

            idx = min(range(n), key=lambda i: count[i])
        count[idx] += 1
        ans.append(idx + 1)

    print(*ans)


if __name__ == '__main__':
    sys.exit(main())
