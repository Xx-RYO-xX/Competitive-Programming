import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    word = set()
    
    s = defaultdict(int)
    for _ in range(n):
        st = input()
        s[st] += 1
        word.add(st)
    
    m = int(input())
    t = defaultdict(int)
    for _ in range(m):
        tt = input()
        t[tt] += 1
        word.add(tt)
    
    ans = 0
    for w in word:
        ans = max(ans, s[w]-t[w])
    
    print(ans)


if __name__ == '__main__':
    main()
