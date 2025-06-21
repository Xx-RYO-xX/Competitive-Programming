import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate
    n = int(input())
    d = list(map(int, input().split()))
    accm = [0]+list(accumulate(d))
    
    for i in range(n-1):
        ans = []
        for j in range(i+1, n):
            ans.append(str(accm[j] - accm[i]))
        
        print(" ".join(ans))


if __name__ == '__main__':
    main()
