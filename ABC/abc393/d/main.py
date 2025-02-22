import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input().strip()

    one = [i for i, ch in enumerate(s) if ch == '1']

    k = len(one)
    m = k // 2  
    mid = one[m]
    
    ans = 0
    for i, pos in enumerate(one):
        target = mid-m+i
        ans += abs(pos-target)
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
