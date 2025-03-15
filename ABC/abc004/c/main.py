import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())%60
    ans = [i for i in range(1, 7)]
    for i in range(n):
        idx1 = i%5
        idx2 = i%5 + 1
        
        tmp = ans[idx1]
        ans[idx1] = ans[idx2]
        ans[idx2] = tmp
    
    print(*ans, sep="")


if __name__ == '__main__':
    main()
