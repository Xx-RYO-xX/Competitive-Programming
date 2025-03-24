import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))

    count_a = Counter(a)
    max_num = -1    
    ans = -1 

    for i in range(n):
        if count_a[a[i]] == 1 and a[i] > max_num:
            max_num = a[i]
            ans = i+1

    print(ans)


if __name__ == '__main__':
    sys.exit(main())
