import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    s = list(input())
    ans = 0
    for i in range(n-2):
        if "".join(s[i:i+3]) == "ABC":
            ans += 1
    # print(ans)
    for _ in range(q):
        x, c = input().split()
        x = int(x)-1
        s[x] = c
        if 

if __name__ == '__main__':
    main()
