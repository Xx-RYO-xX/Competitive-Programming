import sys

sys.setrecursionlimit(10**9)

2
def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    ans = []
    count = 0

    def calc(idx, lst):
        nonlocal count
        if idx == n:
            count += 1
            ans.append(lst.copy())
            return
        start = 1 if idx == 0 else lst[-1] + 10
        if start > m:
            return
        for num in range(start, m - 10*(n - idx -1) +1):
            lst.append(num)
            calc(idx + 1, lst)
            lst.pop()

    calc(0, [])
    
    print(count)
    for ANS in ans:
        print(' '.join(map(str, ANS)))

if __name__ == '__main__':
    main()
