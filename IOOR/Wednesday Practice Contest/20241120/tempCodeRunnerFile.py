import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    reel = [set() for i in range(10)]
    for _ in range(n):
        s = input()
        for i in range(10):
            num = int(s[i])
            ii = i
            while ii in reel[num]:
                ii += 10

            reel[num].add(ii)
    
    ans = float("inf")
    for _ in range(10):
        ans = min(ans, max(reel[i]))
    print(ans)



if __name__ == '__main__':
    main()
