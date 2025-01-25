import sys


def input():return sys.stdin.readline().rstrip()


def can_finish(n, a):
    arr = a[:]
    i = 0
    while i < n:
        while arr[i] > 0:
            if arr[i] >= 3:
                arr[i] -= 3
            elif i+2 < n and arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
                arr[i] -= 1
                arr[i+1] -= 1
                arr[i+2] -= 1
            else:
                return False
        i += 1
    return True


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split())) 
    
    if 2000 < n:
        return

    ans = []
    for K in range(n):
        a[K] += 1
        if can_finish(n, a):
            ans.append(K+1)
        a[K] -= 1

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    sys.exit(main())
