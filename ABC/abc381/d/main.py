import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    
    i = 0
    ans = 0
    count = 0
    sonzai = set()
    idx = dict()
    while i < n-1:
        # print(i)
        # print(a[i] == a[i+1])
        if a[i] == a[i+1]:
            if a[i] not in sonzai:
                count += 2
                sonzai.add(a[i])
                idx[a[i]] = i
                ans = max(ans, count)
            else:
                ans = max(ans, count)
                count = 0
                sonzai.clear()
                i = idx[a[i]]
            i += 2
        else:
            ans = max(ans, count)
            count = 0
            sonzai.clear()
            if i-1 != -1 and a[i-1] == a[i]:
                i -= 1
            else:
                i += 1
    # print(sonzai)
    print(ans)
    
if __name__ == '__main__':
    main()
