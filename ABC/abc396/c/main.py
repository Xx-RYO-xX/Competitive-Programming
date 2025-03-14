import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    b = sorted(map(int, input().split()), reverse=True)
    w = sorted(map(int, input().split()), reverse=True)

    accm_b = [0]*(n+1)
    for i in range(1, n+1):
        accm_b[i] = accm_b[i-1] + b[i-1]

    accm_max_b = [float('-inf')]*(n+1)
    accm_max_b[n] = accm_b[n]
    for i in range(n-1, -1, -1):
        accm_max_b[i] = max(accm_b[i], accm_max_b[i+1])

    accm_w = [0]*(m+1)
    for i in range(1, m+1):
        accm_w[i] = accm_w[i-1] + w[i-1]

    ans = float('-inf')

    for k in range(0, min(n, m)+1):
        tmp = accm_max_b[k] + accm_w[k]
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
