import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    from collections import Counter
    ans = sum(a)
    a = Counter(a)
    # print(a)
    # print(ans)
    for _ in range(q):
        b, c = map(int, input().split())
        try:
            bb = a.pop(b)
        except:
            bb = 0
        a[c] += bb
        # print(a)
        ans = ans-b*bb+c*bb
        print(ans)




if __name__ == '__main__':
    sys.exit(main())
