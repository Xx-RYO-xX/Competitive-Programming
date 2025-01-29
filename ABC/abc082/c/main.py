import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    n = int(input())
    a = Counter(map(int, input().split()))
    
    ans = 0
    for key in a:
        value = a[key]
        if key == value:
            continue
        elif key < value:
            ans += value - key
        else:
            ans += value
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
