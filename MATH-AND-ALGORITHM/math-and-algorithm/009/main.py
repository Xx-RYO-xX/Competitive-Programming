import sys 


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    dp = [False] * (s + 1)
    dp[0] = True
    
    for num in a:
        for i in range(s, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    print("Yes" if dp[s] else "No")


if __name__ == '__main__':
    main()
