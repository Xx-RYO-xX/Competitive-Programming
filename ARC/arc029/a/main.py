import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    t = []
    for _ in range(n):
        t.append(int(input()))
    
    sum_t = sum(t)
    max_t = max(t)
    ans = max(max_t, (sum_t + 1) // 2)
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
