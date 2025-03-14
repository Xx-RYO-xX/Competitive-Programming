import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))

    num_to_idx = defaultdict(lambda: -1)
    ans = float('inf')

    for i in range(n):
        if num_to_idx[a[i]] != -1:
            ans = min(ans, i-num_to_idx[a[i]]+1)
        num_to_idx[a[i]] = i

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    sys.exit(main())
