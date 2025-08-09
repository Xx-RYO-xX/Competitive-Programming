import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    ans = 0.0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            x = s[i:j]
            if len(x) >= 3 and x[0] == 't' and x[-1] == 't':
                tans = (x.count("t")-2)/(len(x)-2)
                ans = max(ans, tans)
    
    print(ans)


if __name__ == '__main__':
    main()
