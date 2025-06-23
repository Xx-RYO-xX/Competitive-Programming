import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    alls = 0
    if n <= k:
        alls = k//n
        k -= n*alls
    a_to_num = {a[i]: alls for i in range(n)}
    
    for atn in sorted(a_to_num):
        if 0 < k:
            a_to_num[atn] += 1
            k -= 1
        else:
            break
    
    for A in a:
            print(a_to_num[A])


if __name__ == '__main__':
    main()
